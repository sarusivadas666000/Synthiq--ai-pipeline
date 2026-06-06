from src.decoder_client import DecoderClient
from src.processors import TextProcessor
from src.client import AIClient
from src.models import PipelineOutput
import time


class Bot:
    def __init__(self):
        self.decoder = DecoderClient()
        self.processor = TextProcessor(chunk_size=300, overlap=30)
        self.ai = AIClient()

    def run(self, url: str, max_chunks: int = 5) -> PipelineOutput:
        """Full pipeline: fetch → chunk → generate Q&A → return output."""

        # Step 1 - Fetch document
        print(f"\n📥 Fetching content from: {url}")
        document = self.decoder.fetch_from_url(url)
        print(f"✅ Fetched {len(document.content)} characters")

        # Step 2 - Split into chunks
        print(f"\n✂️  Splitting into chunks...")
        chunks = self.processor.process(document)
        print(f"✅ Created {len(chunks)} chunks")

        # Step 3 - Process only first N chunks (to save API quota)
        chunks_to_process = chunks[:max_chunks]
        print(f"\n🤖 Generating Q&A for {len(chunks_to_process)} chunks...")

        output = PipelineOutput(
            document_id=document.id,
            source=url,
            chunks=chunks_to_process,
            status="processing"
        )

        # Step 4 - Generate Q&A pairs for each chunk
        for i, chunk in enumerate(chunks_to_process):
            print(f"  Processing chunk {i+1}/{len(chunks_to_process)}...")
            try:
                qa_pairs = self.ai.generate_qa_pairs(chunk)
                output.qa_pairs.extend(qa_pairs)
                time.sleep(1)  # avoid hitting rate limits
            except Exception as e:
                print(f"  ⚠️  Skipping chunk {i+1}: {e}")

        output.status = "completed"
        print(f"\n✅ Done! Generated {len(output.qa_pairs)} Q&A pairs")
        return output
