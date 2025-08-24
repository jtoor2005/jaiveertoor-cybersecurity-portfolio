import pandas as pd

def _is_adminish(text: str) -> bool:
    t = (text or "").lower()
    return "admin" in t or "domain admin" in t or "system admin" in t

def find_admins_without_mfa(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for _, r in df.iterrows():
        role_admin = _is_adminish(r["role"])
        group_admin = _is_adminish(r["group"])
        mfa = (r["mfa_status"] or "").strip().lower()
        if (role_admin or group_admin) and mfa not in ("enabled", "enrolled", "on"):
            rows.append({
                "username": r["username"],
                "violation_type": "Admin without MFA",
                "details": f"Role='{r['role']}', Group='{r['group']}', MFA='{r['mfa_status']}'",
                "risk_level": "High"
            })
    return pd.DataFrame(rows)
