import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "sqlite:///data/db/bluestock_mf.db"
)

# Load cleaned files
nav = pd.read_csv(
    "data/processed/cleaned_nav_history.csv"
)

investor = pd.read_csv(
    "data/processed/cleaned_investor_transactions.csv"
)

performance = pd.read_csv(
    "data/processed/cleaned_scheme_performance.csv"
)

# Save into SQLite
nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

investor.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Database Loaded Successfully!")