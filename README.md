# PocketPilot — Gemini-powered Personal Finance Concierge

PocketPilot is a minimal, runnable multi-agent personal finance assistant that uses Google Gemini (when available) for LLM reasoning. It ingests a CSV, categorizes transactions (rules + LLM fallback), summarizes the month, stores simple memory, and outputs a markdown report.

## Quickstart
1. (Optional) Set your Gemini API key in the environment:
```bash
export GEMINI_API_KEY="your_gemini_api_key"
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Run the demo:
```bash
python run_agent.py --csv examples/sample_statement.csv
```
Report is written to `output/report.md`.

Notes:
- If `GEMINI_API_KEY` is not set, the code will use rule-based categorization only.
- Do NOT commit API keys.
