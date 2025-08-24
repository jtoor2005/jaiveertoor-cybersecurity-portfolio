# 🛡️ Active Directory Policy Violation Analyzer

*Automated Active Directory policy audit tool that detects dormant accounts, missing MFA, and access violations, producing compliance reports and charts.*

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
- Enforces **Departmental Policies**  
  - Interns cannot have admin rights  
  - Non-IT users should not have admin roles  
  - Managers must have MFA enabled  

---

## 📂 Project Structure


📊 Sample Output

Violations Report (CSV)

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



