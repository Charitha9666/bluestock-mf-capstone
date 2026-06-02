import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///data/db/bluestock_mf.db")

# Load cleaned CSV
df = pd.read_csv("data/processed/02_nav_history_clean.csv")

# Save to database
df.to_sql("fact_nav", engine, if_exists="replace", index=False)

print("Database created successfully!")