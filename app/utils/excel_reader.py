import pandas as pd

def read_and_clean_excel(file):
    df = pd.read_excel(file)
    df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
    return df
