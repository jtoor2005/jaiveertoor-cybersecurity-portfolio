from datetime import datetime
import pandas as pd
from pathlib import Path

DATE_FMT = "%Y-%m-%d"

def load_ad_csv(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, dtype=str)
    # Normalize columns
    expected = ["username","dept","last_login","role","group","mfa_status"]
    missing = [c for c in expected if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns in input CSV: {missing}")
    # Clean whitespace & case
    for c in expected:
        df[c] = df[c].astype(str).str.strip()
    return df

def parse_date(d: str) -> datetime | None:
    try:
        return datetime.strptime(d, DATE_FMT)
    except Exception:
        return None

def days_since(date_str: str, ref: datetime | None = None) -> int | None:
    dt = parse_date(date_str)
    if not dt:
        return None
    ref = ref or datetime.now()
    return (ref - dt).days

def ensure_dir(path: str):
    Path(path).mkdir(parents=True, exist_ok=True)

def write_csv(df: pd.DataFrame, path: str):
    ensure_dir(str(Path(path).parent))
    df.to_csv(path, index=False)
