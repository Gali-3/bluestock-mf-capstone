import pandas as pd

files = [
    "01_fund_master.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv"
]

for file in files:
    print("\n" + "="*50)
    print(file)

    df = pd.read_csv(f"data/raw/{file}")

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nShape:")
    print(df.shape)

    print("\nFirst 5 Rows:")
    print(df.head())