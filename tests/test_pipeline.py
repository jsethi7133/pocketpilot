from agents.orchestrator import Orchestrator

def test_pipeline_runs(tmp_path):
    orch = Orchestrator()
    out = orch.run_pipeline('examples/sample_statement.csv')
    assert out.endswith('report.md')
