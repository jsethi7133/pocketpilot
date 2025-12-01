import argparse
from agents.orchestrator import Orchestrator

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--csv', type=str, default='examples/sample_statement.csv')
    args = parser.parse_args()

    orch = Orchestrator()
    out = orch.run_pipeline(args.csv)
    print('Report written to:', out)

if __name__ == '__main__':
    main()
