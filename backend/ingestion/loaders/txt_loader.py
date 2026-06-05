from pathlib import Path
from typing import List, Dict


class TXTLoader:
    """
    Production-grade TXT loader.

    Responsibilities:
    - Read .txt files safely
    - Return structured document format
    - Keep metadata for traceability
    """

    def __init__(self, encoding: str = "utf-8"):
        self.encoding = encoding

    def load(self, file_path: str) -> List[Dict]:
        """
        Load a TXT file and return structured documents.
        """

        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(f"TXT file not found: {file_path}")

        if path.suffix.lower() != ".txt":
            raise ValueError("Only .txt files are supported")

        with open(path, "r", encoding=self.encoding) as f:
            text = f.read()

        # Basic normalization
        text = text.strip()

        return [
            {
                "content": text,
                "metadata": {
                    "source_type": "txt",
                    "file_name": path.name,
                    "file_path": str(path.resolve()),
                },
            }
        ]