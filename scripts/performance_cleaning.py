import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Original Shape:", df.shape)

cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in cols:
    df[col] = pd.to_numeric(
        df[col],
        errors="coerce"
    )

df = df[
    (df["expense_ratio_pct"] >= 0.1)
    &
    (df["expense_ratio_pct"] <= 2.5)
]

df.to_csv(
    "data/processed/cleaned_scheme_performance.csv",
    index=False
)

print("Performance Cleaning Completed!")
print("Final Shape:", df.shape)