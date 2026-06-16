from abc import ABC, abstractmethod
from typing import List, Dict, Any

class VectorStoreAbstraction(ABC):
    """
    Abstract base class for vector stores to allow easy swapping of underlying technologies (e.g. FAISS -> Pinecone).
    """

    @abstractmethod
    def add_project(self, project: Dict[str, Any]) -> None:
        """Embed and add a project into the vector store."""
        pass

    @abstractmethod
    def search_projects(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        """Search the vector store for the top_k most similar projects given a query string."""
        pass
