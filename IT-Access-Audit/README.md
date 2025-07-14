# 🔐 Access Audit Dashboard – Power BI

This Power BI dashboard provides a visual audit of user access and risk across an organization. It's designed to help identify high-risk users, monitor MFA adoption, and support internal IT audits or compliance checks.

---

## 📊 Features

- **Slicers for filtering by:**
  - Department
  - Role
  - Admin Access (Y/N)
  - Risk Level (Low/Medium/High)

- **Visualizations include:**
  - Pie chart for MFA Enabled vs Disabled
  - Donut chart for Risk Level distribution
  - Interactive table showing:
    - Username
    - Department & Role
    - MFA status
    - Admin access
    - Password last changed
    - Last login
    - Termination date
    - Risk score & level

---

## 📁 Data Source

The dashboard is based on an Excel file: `user_access_inventory.xlsx`

### Required Columns:
- `Username`
- `Department`
- `Role`
- `MFA Enabled`
- `Password Last Changed`
- `Last Login`
- `Termination Date`
- `Admin Access`

---

## 🧠 Risk Scoring Logic

Each user is assigned a **Total Risk Score** based on the following formula:

```excel
=IF([MFA Enabled]="N",1,0)
 + IF(TODAY()-[Password Last Changed]>90,1,0)
 + IF(TODAY()-[Last Login]>60,1,0)
 + IF(ISBLANK([Termination Date]),0,1)
 + IF([Admin Access]="Y",1,0)

## Risk Level Classification

| Score | Risk Level |
| ----- | ---------- |
| 0     | Low        |
| 1–2   | Medium     |
| 3+    | High       |

## How to Use

1. Open Access_Audit_Dashboard.pbix in Power BI Desktop.

2. Click Refresh to load the latest data from Excel.

3. Use the slicers to filter by Department, Role, Admin Access, or Risk Level.

4. Analyze the charts and user access table to identify risks.

## ✅ Use Cases

- Internal IT audits
- User access reviews (e.g., SOX, ISO 27001)
- MFA enforcement tracking
- Access risk reporting for compliance teams
