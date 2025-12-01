import pandas as pd

class SummaryAgent:
    def summarize(self, df):
        df = df.copy()
        if 'date' in df.columns:
            df['month'] = df['date'].dt.to_period('M')
        grp = df.groupby('category').amount.sum().to_dict()
        total = float(df['amount'].sum()) if not df.empty else 0.0
        return {'by_category': grp, 'total': total}
