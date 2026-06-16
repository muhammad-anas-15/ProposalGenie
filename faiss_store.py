from typing import List, Dict, Any
from vector_store import VectorStoreAbstraction
from langchain_community.vectorstores import FAISS
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
import os

from core.config import settings

class LocalFAISSVectorStore(VectorStoreAbstraction):
    """
    Implementation of VectorStoreAbstraction using FAISS for local persistence.
    """
    def __init__(self, index_path: str):
        self.index_path = index_path
        self.embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001" , google_api_key=settings.GOOGLE_API_KEY)
        if os.path.exists(index_path):
            self.vector_store = FAISS.load_local(index_path, self.embeddings, allow_dangerous_deserialization=True)
        else:
            self.vector_store = None

    def _convert_to_doc(self, project: Dict[str, Any]) -> Document:
        skills = project.get('skills', [])
        techs = project.get('technologies', [])
        skills_str = ", ".join(skills) if skills else ""
        techs_str = ", ".join(techs) if techs else ""
        
        content = f"Project Name: {project.get('project_name', '')}\n" \
                  f"Industry: {project.get('industry', '')}\n" \
                  f"Skills: {skills_str}\n" \
                  f"Technologies: {techs_str}\n" \
                  f"Problem: {project.get('problem', '')}\n" \
                  f"Solution: {project.get('solution', '')}\n" \
                  f"Results: {project.get('results', '')}"
                  
        return Document(page_content=content, metadata={
            "id": project.get("id", "Unknown ID"),
            "project_url": project.get("project_url", ""),
            "project_name": project.get("project_name", "Unknown Project"),
            "tech_stack": techs_str 
        })

    def add_project(self, project: Dict[str, Any]) -> None:
        doc = self._convert_to_doc(project)
        if self.vector_store is None:
            self.vector_store = FAISS.from_documents([doc], self.embeddings)
        else:
            self.vector_store.add_documents([doc])
        
        self.vector_store.save_local(self.index_path)

    def search_projects(self, query: str, top_k: int = 3) -> List[Dict[str, Any]]:
        if not self.vector_store:
            return []
        
        results = self.vector_store.similarity_search(query, k=top_k)
        docs = []
        for res in results:
            docs.append({
                "content": res.page_content,
                "metadata": res.metadata
            })
        return docs
