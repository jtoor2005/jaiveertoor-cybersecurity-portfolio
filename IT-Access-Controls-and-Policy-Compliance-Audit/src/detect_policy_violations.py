import pandas as pd

def _contains_admin(text: str) -> bool:
    return "admin" in (text or "").lower()

def find_policy_violations(df: pd.DataFrame) -> pd.DataFrame:
    """
    Example departmental rules:
      - Interns must never have admin roles or be in Admins group (High).
      - Non-IT users with admin roles/groups are violations (High).
      - Any '*Manager' must have MFA enabled (High).
    """
    rows = []
    for _, r in df.iterrows():
        dept = (r["dept"] or "").strip().lower()
        role = (r["role"] or "").strip()
        group = (r["group"] or "").strip()
        mfa = (r["mfa_status"] or "").strip().lower()

        # Intern rule
        if dept == "intern" and (_contains_admin(role) or _contains_admin(group)):
            rows.append({
                "username": r["username"],
                "violation_type": "Dept policy: Intern with admin access",
                "details": f"Dept=Intern, Role='{role}', Group='{group}'",
                "risk_level": "High"
            })

        # Non-IT having admin access
        if dept != "it" and (_contains_admin(role) or _contains_admin(group)):
            rows.append({
                "username": r["username"],
                "violation_type": "Dept policy: Non-IT admin access",
                "details": f"Dept='{r['dept']}', Role='{role}', Group='{group}'",
                "risk_level": "High"
            })

        # Managers must have MFA
        if role.lower().endswith("manager") and mfa not in ("enabled", "enrolled", "on"):
            rows.append({
                "username": r["username"],
                "violation_type": "Dept policy: Manager without MFA",
                "details": f"Role='{role}', MFA='{r['mfa_status']}'",
                "risk_level": "High"
            })

    return pd.DataFrame(rows)
