from abc import ABC, abstractmethod


class BaseLoader(ABC):
    """
    Base class for all document loaders.
    PDF, TXT, Web loaders will inherit this.
    """

    @abstractmethod
    def load(self, source: str) -> str:
        """
        Load raw text from any source.

        Args:
            source: file path or URL

        Returns:
            Extracted text content
        """
        pass