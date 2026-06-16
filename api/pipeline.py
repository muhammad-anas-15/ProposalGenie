from schemas import PipelineResult
from gemini_service import GeminiService
from faiss_store import LocalFAISSVectorStore
from agents.analyzer import JobAnalyzerAgent
from agents.skill_matcher import SkillMatcherAgent
from agents.retriever import PortfolioRetrieverAgent
from agents.generator import ProposalGeneratorAgent
from agents.reviewer import ProposalReviewerAgent

class PipelineOrchestrator:
    def __init__(self, gemini: GeminiService, vector_store: LocalFAISSVectorStore):
        self.analyzer = JobAnalyzerAgent(gemini)
        self.matcher = SkillMatcherAgent()
        self.retriever = PortfolioRetrieverAgent(vector_store)
        self.generator = ProposalGeneratorAgent(gemini)
        self.reviewer = ProposalReviewerAgent(gemini)
        
    def run(self, job_title: str, job_text: str, profile_skills: list[str]) -> PipelineResult:
        print("Running Job Analyzer...")
        analysis = self.analyzer.analyze(job_title, job_text)
        
        print("Running Skill Matcher...")
        match = self.matcher.match(analysis, profile_skills)
        
        print("Running Portfolio Retriever...")
        projects = self.retriever.retrieve(analysis)
        
        print("Running Proposal Generator...")
        draft = self.generator.generate(analysis, match, projects)
        
        print("Running Proposal Reviewer...")
        final = self.reviewer.review(draft)
        
        return PipelineResult(
            analysis=analysis,
            match_result=match,
            retrieved_projects=projects,
            proposal=final
        )
