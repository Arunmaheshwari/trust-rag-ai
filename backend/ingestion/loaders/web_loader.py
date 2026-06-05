import httpx
from bs4 import BeautifulSoup
from typing import Dict, List


class WebLoader:
    """
    Production-grade Web loader.

    Responsibilities:
    - Fetch web page content
    - Clean HTML
    - Return structured RAG-ready document
    """

    def __init__(self, timeout: int = 10):
        self.timeout = timeout

    def load(self, url: str) -> List[Dict]:
        """
        Fetch and extract clean text from a web page.
        """

        try:
            response = httpx.get(url, timeout=self.timeout)
            response.raise_for_status()
        except Exception as e:
            raise Exception(f"Failed to fetch URL {url}: {str(e)}")

        try:
           soup = BeautifulSoup(response.text, "lxml")
        except Exception:
           soup = BeautifulSoup(response.text, "html.parser")

        # Remove script/style
        for tag in soup(["script", "style", "noscript"]):
            tag.decompose()

        text = soup.get_text(separator=" ")
        text = " ".join(text.split())

        return [
            {
                "content": text,
                "metadata": {
                    "source_type": "web",
                    "url": url,
                    "title": soup.title.string if soup.title else None,
                },
            }
        ]