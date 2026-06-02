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


# Clean remaining files

files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

for file in files:
    df = pd.read_csv(f"data/raw/{file}")

    df = df.drop_duplicates()

    output_file = file.replace(".csv", "_clean.csv")

    df.to_csv(
        f"data/processed/{output_file}",
        index=False
    )

    print(output_file, "saved")