# Data Dictionary

## fact_nav

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Fund identifier |
| date | DATE | NAV date |
| nav | REAL | Net Asset Value |

## fact_transactions

| Column | Type | Description |
|----------|----------|----------|
| investor_id | TEXT | Investor ID |
| transaction_date | DATE | Transaction Date |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount_inr | REAL | Amount invested |

## fact_performance

| Column | Type | Description |
|----------|----------|----------|
| amfi_code | INTEGER | Fund identifier |
| return_1yr_pct | REAL | 1 Year Return |
| return_3yr_pct | REAL | 3 Year Return |
| return_5yr_pct | REAL | 5 Year Return |
| expense_ratio_pct | REAL | Expense Ratio |
| aum_crore | REAL | Assets Under Management |