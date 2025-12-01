from pathlib import Path
def export_report(df, summary, recs, out_path='output/report.md'):
    Path('output').mkdir(exist_ok=True)
    with open(out_path, 'w') as f:
        f.write('# PocketPilot Report\n\n')
        f.write('## Summary by category\n')
        for k, v in summary['by_category'].items():
            f.write(f'- {k}: {v}\n')
        f.write(f"\n**Total:** {summary['total']}\n\n")
        f.write('## Top Transactions (sample)\n')
        if not df.empty:
            f.write(df[['date','description','amount','category']].head(10).to_markdown(index=False))
            f.write('\n\n')
        f.write('## Recommendations\n')
        for r in recs:
            f.write(f'- {r}\n')
    return out_path
