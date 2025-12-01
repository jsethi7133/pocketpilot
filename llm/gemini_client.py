import os
try:
    import google.generativeai as genai
except Exception:
    genai = None

class GeminiClient:
    def __init__(self):
        self.api_key = os.environ.get('GEMINI_API_KEY')
        if self.api_key and genai:
            genai.configure(api_key=self.api_key)
            self.model = 'gemini-1.5'  # adjust model name as needed
            self.available = True
        else:
            self.available = False

    def generate(self, prompt: str) -> str:
        if self.available:
            # Minimal call to Google Generative AI; SDK response shapes vary by version.
            resp = genai.generate_text(model=self.model, input=prompt)
            # Try to extract text from common response fields
            if hasattr(resp, 'text') and resp.text:
                return resp.text
            # fallback to string conversion
            return str(resp)
        # Fallback: simple heuristic echo (no LLM)
        # Return short rule-based suggestions for demonstration if Gemini not configured.
        if 'recommend' in prompt.lower():
            return '1. Automate 10% savings.\n2. Reduce subscriptions.\n3. Cook at home twice a week.'
        if 'classify' in prompt.lower() or 'category' in prompt.lower():
            # Try simple keyword mapping
            p = prompt.lower()
            if 'swiggy' in p or 'zomato' in p: return 'Food'
            if 'uber' in p or 'ola' in p: return 'Transport'
            if 'amazon' in p: return 'Shopping'
            return 'Other'
        return 'No response (Gemini not configured)'
