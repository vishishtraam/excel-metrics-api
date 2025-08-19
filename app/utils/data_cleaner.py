import pandas as pd
import os

def clean_file(file_path: str, cleaned_dir: str):
    # Load file
    df = pd.read_excel(file_path)

    # Example cleaning
    df = df.dropna()
    df = df.drop_duplicates()

    # Save cleaned file in CLEANED_DIR
    cleaned_filename = f"cleaned_{os.path.basename(file_path)}"
    cleaned_path = os.path.join(cleaned_dir, cleaned_filename)
    df.to_excel(cleaned_path, index=False)

    return cleaned_path, df
