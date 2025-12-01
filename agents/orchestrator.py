import logging
from tools.csv_parser import load_transactions
from agents.parser_agent import ParserAgent
from agents.categorizer_agent import CategorizerAgent
from agents.summary_agent import SummaryAgent
from agents.insights_agent import InsightsAgent
from tools.exporter import export_report
from memory.memory_bank import MemoryBank

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('Orchestrator')

class Orchestrator:
    def __init__(self):
        self.parser = ParserAgent()
        self.categorizer = CategorizerAgent()
        self.summary = SummaryAgent()
        self.insights = InsightsAgent()
        self.memory = MemoryBank()

    def run_pipeline(self, csv_path: str):
        logger.info('Parsing CSV: %s', csv_path)
        df = self.parser.parse(csv_path)
        logger.info('Categorizing transactions')
        categorized = self.categorizer.categorize(df)
        logger.info('Summarizing')
        summary = self.summary.summarize(categorized)
        logger.info('Generating insights')
        recs = self.insights.generate(categorized, summary)
        logger.info('Updating memory')
        self.memory.update_from_summary(summary)
        out = export_report(categorized, summary, recs, out_path='output/report.md')
        return out
