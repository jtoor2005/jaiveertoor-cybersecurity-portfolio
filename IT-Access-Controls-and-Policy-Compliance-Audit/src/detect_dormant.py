import pandas as pd
from datetime import datetime
from .utils import days_since

def find_dormant(df: pd.DataFrame, threshold_days: int = 90, ref_date: datetime | None = None) -> pd.DataFrame:
    rows = []
    for _, r in df.iterrows():
        ds = days_since(r["last_login"], ref_date)
        if ds is not None and ds > threshold_days:
            rows.append({
                "username": r["username"],
                "violation_type": "Dormant account",
                "details": f"Last login {r['last_login']} (~{ds} days ago)",
                "risk_level": "Medium"
            })
    return pd.DataFrame(rows)
