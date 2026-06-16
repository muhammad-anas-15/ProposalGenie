import re
from schemas import JobAnalysis, RetrievedProject
from faiss_store import LocalFAISSVectorStore
from typing import List

class PortfolioRetrieverAgent:
    def __init__(self, vector_store: LocalFAISSVectorStore):
        self.vector_store = vector_store
        
    def retrieve(self, analysis: JobAnalysis) -> List[RetrievedProject]:
        query = f"Category: {analysis.project_category}. Skills: {', '.join(analysis.required_skills)}. Problem: {analysis.summary}"
        results = self.vector_store.search_projects(query, top_k=3)
        
        projects = []
        for r in results:
            content = r['content']
            metadata = r['metadata']
            
            # Use regex to cleanly pull out exactly what belongs in each box
            problem_match = re.search(r'Problem:\s*(.*?)(?=\nSolution:|$)', content, re.DOTALL)
            solution_match = re.search(r'Solution:\s*(.*?)(?=\nResults:|$)', content, re.DOTALL)
            results_match = re.search(r'Results:\s*(.*)', content, re.DOTALL)
            
            # Grab the tech stack we saved in the metadata earlier and turn it back into a list
            tech_stack_str = metadata.get('tech_stack', '')
            skills_list = [s.strip() for s in tech_stack_str.split(',')] if tech_stack_str else []
            
            projects.append(RetrievedProject(
                project_name=metadata.get('project_name', 'Unknown'),
                problem=problem_match.group(1).strip() if problem_match else "Details in content.",
                solution=solution_match.group(1).strip() if solution_match else "",
                results=results_match.group(1).strip() if results_match else "",
                skills=skills_list,
                technologies=[], # We combined these into skills_list above
                project_url=metadata.get('project_url', '')
            ))
            
        return projects