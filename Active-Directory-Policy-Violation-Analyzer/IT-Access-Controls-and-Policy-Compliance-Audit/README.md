# 🛡️ Active Directory Policy Violation Analyzer

*Automated AD audit tool that detects dormant accounts, missing MFA, and access violations, producing compliance reports and charts.*

---

## 📌 Overview
This project simulates an **internal IT audit tool** for analyzing Active Directory (AD) user exports.  
It detects risky accounts and policy violations, then generates a compliance report and visualization.  

🔧 **Built with:** Python, pandas, matplotlib  
📊 **Output:** CSV report + bar chart of violations  

---

## 🚀 Features
- Detects **Dormant Accounts** (no login > 90 days)  
- Flags **Admins Without MFA**  
- Enforces **Departmental Policies**:  
  - Interns cannot have admin rights  
  - Non-IT users should not have admin roles  
  - Managers must have MFA enabled  

---

## 📂 Project Structure

IT-Access-Controls-and-Policy-Compliance-Audit/
│── data/
│ └── ad_export_sample.csv # Mock AD export
│── src/
│ ├── main.py # Entry point
│ ├── utils.py # Helpers (CSV, dates, output)
│ ├── detect_dormant.py # Dormant accounts
│ ├── detect_admin_no_mfa.py # Admins without MFA
│ └── detect_policy_violations.py # Department rules
│── reports/
│ ├── violations_report.csv # Generated violations
│ └── summary_visualization.png # Violation summary chart
│── requirements.txt
│── README.md


---

## ⚡ How to Run

Follow these steps to run the analyzer on your own machine:

### 1. Clone the Repository
```bash
git clone https://github.com/jtoor2005/jaiveertoor-cybersecurity-portfolio.git
cd jaiveertoor-cybersecurity-portfolio/IT-Access-Controls-and-Policy-Compliance-Audit

### 2. Set Up a Virtual Environment (Recommended)

python -m venv .venv
.\.venv\Scripts\activate    # On Windows
# source .venv/bin/activate # On Mac/Linux

### 3. Install Dependencies

pip install -r requirements.txt


### 4. Run the Analyzer

python -m src.main

### 5. View Results

      - 📄 CSV Report: reports/violations_report.csv → Contains all detected violations
      - 📊 Chart: reports/summary_visualization.png → Bar chart of violation types

### 📊 Sample Output

# Violations Report (CSV)

| username | violation\_type              | details                                | risk\_level |
| -------- | ---------------------------- | -------------------------------------- | ----------- |
| jdoe     | Dormant account              | Last login 2024-06-15 (\~434 days ago) | Medium      |
| bjones   | Admin without MFA            | Role='Domain Admin', MFA='Disabled'    | High        |
| bjones   | Dept policy: Intern w/ admin | Dept=Intern, Role=Domain Admin         | High        |
| awilson  | Admin without MFA            | Role='System Admin', MFA='Disabled'    | High        |

Visualization (Bar Chart)

🛠 Skills Demonstrated

     - Python (automation & scripting)

     - pandas (data analysis & CSV processing)

     - matplotlib (data visualization)

     - Identity & Access Management (IAM)

     - Governance, Risk, and Compliance (GRC)

     - IT Audit / Access Review

     - Security Automation

     - Active Directory (simulated)

### 📄 Resume Highlights

     - Built a Python-based internal tool to analyze mock Active Directory user exports for policy violations.

     - Automated detection of dormant accounts, excessive privileges, missing MFA, and departmental access risks.

     - Generated risk classification reports and visualizations to simulate enterprise IT audit procedures.