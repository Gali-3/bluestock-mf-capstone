-- Top 5 funds by AUM
SELECT *
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- Highest 1 year return
SELECT amfi_code, return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- Lowest expense ratio
SELECT amfi_code, expense_ratio_pct
FROM fact_performance
ORDER BY expense_ratio_pct ASC
LIMIT 5;

-- Total transaction amount
SELECT SUM(amount_inr)
FROM fact_transactions;

-- Transactions by type
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- Transactions by state
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state;

-- Average 3 year return
SELECT AVG(return_3yr_pct)
FROM fact_performance;

-- Average 5 year return
SELECT AVG(return_5yr_pct)
FROM fact_performance;

-- Fund count
SELECT COUNT(*)
FROM fact_performance;