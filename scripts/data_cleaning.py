import pandas as pd
import os

RAW_PATH = "data/raw"
PROCESSED_PATH = "data/processed"

os.makedirs(PROCESSED_PATH, exist_ok=True)

# Load NAV History dataset
nav_df = pd.read_csv(f"{RAW_PATH}/02_nav_history.csv")

print("\nColumns:")
print(nav_df.columns)

print("\nData Types:")
print(nav_df.dtypes)

print("\nMissing Values:")
print(nav_df.isnull().sum())

print("\nFirst 5 Rows:")
print(nav_df.head())

# Convert date column
nav_df["date"] = pd.to_datetime(nav_df["date"])

# Sort data
nav_df = nav_df.sort_values(["amfi_code", "date"])

# Remove duplicates
nav_df = nav_df.drop_duplicates()

# Validate NAV > 0
nav_df = nav_df[nav_df["nav"] > 0]

# Save cleaned file
nav_df.to_csv("data/processed/02_nav_history_clean.csv", index=False)

print("\nCleaned file saved successfully!")