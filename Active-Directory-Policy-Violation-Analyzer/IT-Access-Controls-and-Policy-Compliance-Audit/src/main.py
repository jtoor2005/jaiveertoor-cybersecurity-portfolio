import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt

from .utils import load_ad_csv, write_csv, ensure_dir
from .detect_dormant import find_dormant
from .detect_admin_no_mfa import find_admins_without_mfa
from .detect_policy_violations import find_policy_violations

DATA_PATH = Path("data/ad_export_sample.csv")
REPORTS_DIR = Path("reports")
REPORT_CSV = REPORTS_DIR / "violations_report.csv"
REPORT_IMG = REPORTS_DIR / "summary_visualization.png"

def build_report():
    df = load_ad_csv(str(DATA_PATH))

    v1 = find_dormant(df, threshold_days=90)
    v2 = find_admins_without_mfa(df)
    v3 = find_policy_violations(df)

    violations = pd.concat([v1, v2, v3], ignore_index=True)
    if violations.empty:
        print("No violations found.")
    else:
        write_csv(violations, str(REPORT_CSV))
        print(f"Wrote violations CSV -> {REPORT_CSV}")

        # Visualization: count by violation_type
        counts = violations["violation_type"].value_counts()
        ensure_dir(str(REPORTS_DIR))
        plt.figure()
        counts.plot(kind="bar", title="Policy Violations by Type")
        plt.xlabel("Violation Type")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(REPORT_IMG)
        plt.close()
        print(f"Wrote summary chart -> {REPORT_IMG}")

if __name__ == "__main__":
    build_report()
