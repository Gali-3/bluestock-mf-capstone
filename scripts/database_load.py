import pandas as pd
from sqlalchemy import create_engine

# Load cleaned data
df = pd.read_csv("data/processed/cleaned_nav.csv")

# Create SQLite database
engine = create_engine("sqlite:///data/db/mutual_fund.db")

# Save table
df.to_sql(
    "sbi_smallcap_nav",
    engine,
    if_exists="replace",
    index=False
)

print("Database created successfully!")
print("Rows loaded:", len(df))