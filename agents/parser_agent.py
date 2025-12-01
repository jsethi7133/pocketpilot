from tools.csv_parser import load_transactions

class ParserAgent:
    def parse(self, csv_path: str):
        return load_transactions(csv_path)
