# Data Dictionary

## fact_nav

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| amfi_code | INTEGER | Mutual fund scheme code |
| date | DATE | NAV date |
| nav | FLOAT | Net Asset Value |
## fund_master

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| amfi_code | INTEGER | Mutual fund scheme code |
| scheme_name | TEXT | Name of mutual fund scheme |
| fund_house | TEXT | Asset management company |

## investor_transactions

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| investor_id | INTEGER | Unique investor ID |
| transaction_date | DATE | Transaction date |
| transaction_type | TEXT | SIP/Lumpsum/Redemption |
| amount | FLOAT | Transaction amount |

## scheme_performance

| Column Name | Data Type | Description |
|------------|-----------|-------------|
| amfi_code | INTEGER | Mutual fund scheme code |
| return_1y | FLOAT | One year return |
| return_3y | FLOAT | Three year return |
| expense_ratio | FLOAT | Fund expense ratio |

## Source

Data Source: AMFI Mutual Fund Datasets

Project: Bluestock Mutual Fund Analytics Capstone