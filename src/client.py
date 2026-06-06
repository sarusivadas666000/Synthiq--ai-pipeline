import os
from groq import Groq
from dotenv import load_dotenv
from typing import List
from src.models import TextChunk, QAPair

load_dotenv()


class AIClient:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in .env file")
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.1-8b-instant"

    def generate_qa_pairs(self, chunk: TextChunk) -> List[QAPair]:
        prompt = f"""You are a helpful assistant that generates high quality question and answer pairs.

Given the following text, generate 3 question-answer pairs that test understanding of the content.

Text:
{chunk.content}

Respond ONLY in this exact format, nothing else:
Q1: <question>
A1: <answer>
Q2: <question>
A2: <answer>
Q3: <question>
A3: <answer>"""

        response = self.client.chat.completions.create(
            model=self.model,
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}]
        )

        raw_text = response.choices[0].message.content
        return self._parse_qa_response(raw_text, chunk.chunk_id)

    def _parse_qa_response(self, raw_text: str, chunk_id: str) -> List[QAPair]:
        qa_pairs = []
        lines = raw_text.strip().split("\n")
        questions = {}
        answers = {}

        for line in lines:
            line = line.strip()
            if line.startswith("Q") and ":" in line:
                num = line[1]
                questions[num] = line.split(":", 1)[1].strip()
            elif line.startswith("A") and ":" in line:
                num = line[1]
                answers[num] = line.split(":", 1)[1].strip()

        for num in questions:
            if num in answers:
                qa_pairs.append(QAPair(
                    question=questions[num],
                    answer=answers[num],
                    source_chunk_id=chunk_id
                ))

        return qa_pairs
