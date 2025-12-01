# PocketPilot — Personal Finance Concierge Agent

**Track:** Concierge Agents  
**Short:** Automated personal-finance agent that ingests bank CSVs, auto-categorizes transactions, forecasts budgets, and delivers personalized recommendations.

## Why this project
Manual budgeting is time-consuming, error-prone, and often abandoned. PocketPilot automates ingestion, categorization, forecasting, and recommendation so users can make confident financial decisions with minimal effort.

## Features
- Multi-agent architecture: Orchestrator + parallel Categorizer agents + Forecast agent
- Tools: CSV parser, Rules engine, Forecast tool, Export tool
- Sessions & Memory: InMemory session + long-term JSON MemoryBank
- Observability: logging, simple metrics, traceable long-running ops
- Evaluation harness: categorization accuracy & MAPE for budgets

## Repo layout
pocketpilot/
README.md
pocketpilot_agent.py
tools/
csv_tool.py
rules_tool.py
forecast_tool.py
export_tool.py
data/
sample_transactions.csv
sample_transactions_labeled.csv
memory_bank.json
tests/
test_categorization.py
output/
requirements.txt
Dockerfile
run_demo.sh


## Quickstart
1. `git clone <repo>`
2. `python -m venv venv && source venv/bin/activate`
3. `pip install -r requirements.txt`
4. `python pocketpilot_agent.py --demo --csv data/sample_transactions.csv`
5. Check `output/report.md`

## How it works (summary)
1. Upload CSV → Data Parser Agent cleans & normalizes.
2. Parallel Categorizer Agents label transactions (rules + LLM fallback).
3. Budget Agent aggregates and compares historicals (MemoryBank).
4. Forecast Agent runs Python analysis for savings projection.
5. Insights Agent returns actionable recommendations.

## Evaluation
- `tests/test_categorization.py` computes categorization accuracy vs labeled CSV.
- Forecasts assessed via MAPE against holdout months.

## Deployment
- Containerized via `Dockerfile` (included)
- Deploy to Cloud Run or Agent Engine for live use

## Next steps
- Bank API integration, OCR receipts, UI/WhatsApp front-end, richer ML models.

