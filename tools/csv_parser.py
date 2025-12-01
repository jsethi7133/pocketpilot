import pandas as pd

def load_transactions(path: str):
    df = pd.read_csv(path)
    # expected columns: date, description, amount
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
    else:
        df['date'] = pd.NaT
    if 'description' not in df.columns:
        df['description'] = ''
    df['amount'] = pd.to_numeric(df['amount'], errors='coerce').fillna(0.0)
    return df
