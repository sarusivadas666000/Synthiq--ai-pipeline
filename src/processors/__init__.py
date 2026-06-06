import uuid
from typing import List
from src.models import Document, TextChunk


class TextProcessor:
    def __init__(self, chunk_size: int = 500, overlap: int = 50):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def process(self, document: Document) -> List[TextChunk]:
        """Splits a document into overlapping text chunks."""
        words = document.content.split()
        chunks = []
        start = 0

        while start < len(words):
            end = start + self.chunk_size
            chunk_words = words[start:end]
            chunk_text = " ".join(chunk_words)

            chunks.append(TextChunk(
                chunk_id=str(uuid.uuid4()),
                document_id=document.id,
                content=chunk_text,
                token_count=len(chunk_words)
            ))

            start += self.chunk_size - self.overlap

        return chunks
