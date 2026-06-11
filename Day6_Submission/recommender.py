import pandas as pd

df = pd.read_csv("fund_scorecard.csv")

risk = input(
"Enter Risk Appetite (Low/Moderate/High): "
)

result = df.sort_values(
'fund_score',
ascending=False
).head(3)

print(result[
['scheme_name',
'fund_score',
'sharpe_ratio']
])