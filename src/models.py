from pydantic import BaseModel, Field
from typing import Optional, List
from enum import Enum


# ── Document Types ──────────────────────────────────────────
class DocumentType(str, Enum):
    PDF = "pdf"
    WEB = "web"
    TEXT = "text"


# ── A single raw document coming into the system ────────────
class Document(BaseModel):
    id: str
    content: str
    source: str
    doc_type: DocumentType
    metadata: dict = Field(default_factory=dict)


# ── A processed chunk of a document ─────────────────────────
class TextChunk(BaseModel):
    chunk_id: str
    document_id: str
    content: str
    token_count: Optional[int] = None


# ── A single AI-generated QA pair ───────────────────────────
class QAPair(BaseModel):
    question: str
    answer: str
    source_chunk_id: str
    quality_score: Optional[float] = None


# ── Final output of the pipeline ────────────────────────────
class PipelineOutput(BaseModel):
    document_id: str
    source: str
    chunks: List[TextChunk] = []
    qa_pairs: List[QAPair] = []
    status: str = "pending"