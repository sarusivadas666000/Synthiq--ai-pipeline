import requests
from bs4 import BeautifulSoup
from src.models import Document, DocumentType
import uuid


class DecoderClient:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
        }

    def fetch_from_url(self, url: str) -> Document:
        """Fetches a webpage and returns a Document object."""
        print(f"Fetching: {url}")
        response = requests.get(url, headers=self.headers, timeout=10)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        # Remove unwanted tags
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()

        text = soup.get_text(separator="\n")
        cleaned = "\n".join(
            line.strip() for line in text.splitlines() if line.strip()
        )

        return Document(
            id=str(uuid.uuid4()),
            content=cleaned,
            source=url,
            doc_type=DocumentType.WEB,
            metadata={"title": soup.title.string if soup.title else ""}
        )

    def fetch_from_text(self, text: str, source: str = "manual") -> Document:
        """Wraps plain text into a Document object."""
        return Document(
            id=str(uuid.uuid4()),
            content=text,
            source=source,
            doc_type=DocumentType.TEXT
        )
