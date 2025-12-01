import pandas as pd
from tools.rules_engine import RulesEngine
from llm.gemini_client import GeminiClient
from concurrent.futures import ThreadPoolExecutor

class CategorizerAgent:
    def __init__(self):
        self.rules = RulesEngine()
        self.llm = GeminiClient()

    def _classify_row(self, desc):
        # Apply deterministic rules first
        r = self.rules.apply(desc)
        if r != 'uncategorized':
            return r
        # Fallback to LLM if available
        try:
            prompt = f"Classify this transaction description into one category: 'Food, Rent, Transport, Shopping, Subscriptions, Utilities, Income, Other'.\nDescription: {desc}"
            out = self.llm.generate(prompt)
            # sanitize response
            cat = out.strip().split('\n')[0].strip()
            # normalize small variations
            mapping = {'entertainment':'Subscriptions'}
            if cat.lower() in mapping:
                return mapping[cat.lower()]
            return cat
        except Exception:
            return 'Other'

    def categorize(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        # ensure description column
        if 'description' not in df.columns:
            df['description'] = ''
        # run classification in parallel for speed
        with ThreadPoolExecutor(max_workers=4) as ex:
            results = list(ex.map(self._classify_row, df['description'].tolist()))
        df['category'] = results
        return df
