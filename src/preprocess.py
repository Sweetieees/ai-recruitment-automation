import pandas as pd

def load_and_clean_data(file_path: str) -> pd.DataFrame:
    df = pd.read_csv(file_path)

    # Standardize column names
    df.columns = df.columns.str.strip().str.lower()

    # Fill missing values
    text_columns = ["name", "email", "skills", "location", "current_role", "notes"]
    for col in text_columns:
        if col in df.columns:
            df[col] = df[col].fillna("").astype(str).str.strip()

    if "years_experience" in df.columns:
        df["years_experience"] = pd.to_numeric(df["years_experience"], errors="coerce").fillna(0)

    # Standardize text casing where useful
    df["skills"] = df["skills"].str.lower()
    df["current_role"] = df["current_role"].str.lower()
    df["notes"] = df["notes"].str.lower()

    return df