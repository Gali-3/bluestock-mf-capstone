import pandas as pd

df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Original Shape:", df.shape)

df["transaction_type"] = df["transaction_type"].str.strip().str.title()

df = df[df["amount_inr"] > 0]

df["transaction_date"] = pd.to_datetime(
    df["transaction_date"],
    errors="coerce"
)

valid_kyc = ["Verified", "Pending"]

df = df[df["kyc_status"].isin(valid_kyc)]

df.to_csv(
    "data/processed/cleaned_investor_transactions.csv",
    index=False
)

print("Investor Cleaning Completed!")
print("Final Shape:", df.shape)