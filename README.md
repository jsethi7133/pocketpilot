# PocketPilot – Multi-Agent CSV Processor with Gemini

PocketPilot is a lightweight demonstration of a multi-agent system using Gemini.  
It reads a CSV input, processes it via agents and tools, and outputs a report.  
If the Gemini API key is not set, the system falls back to rule-based categorization.

---

## Problem Statement
Real-world tasks often require multiple steps and reasoning.  
Single-prompt AI models cannot coordinate tasks or handle structured data efficiently.  
PocketPilot demonstrates a simple multi-agent workflow that can ingest data, process it, and produce structured output automatically.

---

## Solution
PocketPilot uses a minimal multi-agent system to process CSV files:  

- **Orchestrator Agent**: Routes tasks to the appropriate tool or LLM reasoning.  
- **Tools**:  
  - **Categorization** (rule-based or Gemini LLM)  
  - **Summarization** of results  
- **CLI**: Reads CSV and writes a Markdown report (`output/report.md`).  
- **Fallback**: If Gemini API key is not provided, the system uses rules only.  

---

## Architecture
+---------------------+
| run_agent.py CLI |
+---------+-----------+
|
v
+---------------------+
| Orchestrator Agent |
+---------+-----------+
|
+------+------+
| |
v v
+-------+ +--------+
|Tools | | Gemini |
|Rules | | LLM |
+-------+ +--------+
|
v
output/report.md

yaml
Copy code
- The CLI reads a CSV file and sends it to the orchestrator.  
- The orchestrator routes tasks to tools or the Gemini LLM.  
- The processed results are written to `output/report.md`.

---

## Setup & Usage

1. **Optional:** Set your Gemini API key:
```bash
export GEMINI_API_KEY="your_gemini_api_key"
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the demo with a CSV:

bash
Copy code
python run_agent.py --csv examples/sample_statement.csv
Check the output report:

bash
Copy code
output/report.md
Note: If GEMINI_API_KEY is not set, the system will use rule-based categorization only.
Do NOT commit API keys.

Build
Gemini / LLM: gemini-1.5-flash via LangChain (optional)

Python: Core language for agents, tools, and CLI

Tools: Python functions for categorization and summarization

Orchestrator Agent: Handles workflow routing

CLI interface: Reads CSV and writes report
