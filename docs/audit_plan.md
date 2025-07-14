# IT Access Control Audit Plan

## Objective
To evaluate user access management practices and identify non-compliance with internal IT policies related to:

- MFA enforcement
- Password change frequency
- Account inactivity
- Admin access review
- Terminated user cleanup

## Scope
- 30 mock user accounts from simulated Active Directory export
- Audit timeframe: 2025
- Data fields: username, department, role, password/MFA status, login/termination dates

## Methodology
- Use Excel formulas to calculate:
  - Password age
  - Login age
  - Policy violations (MFA, inactive, admin overdue, etc.)
- Assign risk weights based on policy matrix
- Score each account and generate insights using Power BI
