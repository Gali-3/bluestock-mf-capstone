import pandas as pd

# Load data
df = pd.read_csv("data/raw/SBI_SmallCap_NAV.csv")

print("Original Shape:", df.shape)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# Convert date column
df["date"] = pd.to_datetime(df["date"], dayfirst=True)

# Sort by date
df = df.sort_values("date")

# Save cleaned data
df.to_csv("data/processed/cleaned_nav.csv", index=False)

print("\nCleaning Completed Successfully!")
print(df.head())