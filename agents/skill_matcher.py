from schemas import JobAnalysis, SkillMatchResult

class SkillMatcherAgent:
    def match(self, analysis: JobAnalysis, profile_skills: list[str]) -> SkillMatchResult:
        # 1. Clean and lowercase the lists
        required = [s.lower().strip() for s in analysis.required_skills]
        profile = [s.lower().strip() for s in profile_skills]
        
        matching = []
        missing = []
        
        # 2. Smarter matching logic (checks for overlapping words)
        for req in required:
            is_match = any((req in p) or (p in req) for p in profile)
            if is_match:
                matching.append(req)
            else:
                missing.append(req)
        
        # 3. Calculate score
        score = 0
        if len(required) > 0:
            score = int((len(matching) / len(required)) * 100)
        else:
            score = 100
            
        reasoning = f"Matched {len(matching)} out of {len(required)} required skills. Missing: {', '.join(missing) if missing else 'None'}."
            
        return SkillMatchResult(
            match_score=score,
            matching_skills=matching, # Pydantic will auto-convert this to a list
            missing_skills=missing,
            reasoning=reasoning
        )