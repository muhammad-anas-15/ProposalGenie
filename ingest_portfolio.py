import asyncio
from typing import List, Dict, Any
from core.config import settings
from database import AsyncSessionLocal
from models.portfolio import PortfolioProject
from faiss_store import LocalFAISSVectorStore
from sqlalchemy import select

def ingest_portfolio_to_vectorstore():
    print(f"Initializing FAISS at {settings.FAISS_INDEX_PATH}...")
    vector_store = LocalFAISSVectorStore(settings.FAISS_INDEX_PATH)
    
    # We could fetch from database here, but for testing we'll use a sample
    sample_projects = [
        {
            "id": 1,
            "project_name": "E-Commerce Replatforming",
            "industry": "Retail",
            "skills": ["Python", "FastAPI", "React", "PostgreSQL"],
            "technologies": ["AWS", "Docker"],
            "problem": "Legacy monolith was too slow to handle Black Friday traffic.",
            "solution": "Migrated to a microservices architecture using FastAPI, resulting in 10x faster response times.",
            "results": "Zero downtime during peak sales, 20% increase in conversion rate.",
            "project_url": "https://example.com/project1"
        },
        {
            "id": 2,
            "project_name": "Real-time Supply Chain Dashboard",
            "industry": "Logistics",
            "skills": ["JavaScript", "TypeScript", "Node.js", "GraphQL"],
            "technologies": ["GCP", "Kubernetes", "Redis"],
            "problem": "Operational data was fragmented and delayed by 24 hours.",
            "solution": "Built a real-time event streaming pipeline using Redis and GraphQL to aggregate updates instantly.",
            "results": "Saved 15 hours of manual reporting per week and reduced shipping delays by 12%.",
            "project_url": "https://example.com/project2"
        }
    ]

    for project in sample_projects:
        print(f"Ingesting project: {project['project_name']}")
        vector_store.add_project(project)
        
    print("Ingestion complete.")
    
    # Validate
    print("\nTesting retrieval. Query: 'Looking for someone to build a fast python backend for a store'")
    results = vector_store.search_projects("Looking for someone to build a fast python backend for a store", top_k=1)
    
    for r in results:
        print(f"Available metadata keys: {r['metadata'].keys()}")
        print(f"Content: {r['content'][:150]}...\n")

if __name__ == "__main__":
    ingest_portfolio_to_vectorstore()
