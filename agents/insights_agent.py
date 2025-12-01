from llm.gemini_client import GeminiClient

class InsightsAgent:
    def __init__(self):
        self.llm = GeminiClient()

    def generate(self, df, summary):
        # Compose a prompt summarizing category spend and ask Gemini for actionable tips.
        prompt = f"Monthly spending by category: {summary['by_category']}. Total: {summary['total']}. Provide up to 4 short actionable recommendations to improve savings."
        try:
            out = self.llm.generate(prompt)
            lines = [l.strip() for l in out.split('\n') if l.strip()]
            return lines if lines else ['No recommendations.']
        except Exception:
            # Fallback simple heuristics
            recs = []
            for cat, amt in summary['by_category'].items():
                if amt > summary['total'] * 0.25:
                    recs.append(f"High spend in {cat}: consider trimming subscriptions or discretionary use.")
            if not recs:
                recs = ['Spending looks balanced. Consider automating savings of 10% of income.']
            return recs
