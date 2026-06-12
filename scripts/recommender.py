import pandas as pd

scheme_perf = pd.read_csv(
    "../data/processed/07_scheme_performance_clean.csv"
)

risk_level = input("Enter Risk Level (Low/Moderate/High): ")

recommended = scheme_perf[
    scheme_perf['risk_grade'] == risk_level
].sort_values(
    by='sharpe_ratio',
    ascending=False
).head(3)

print("\nTop 3 Recommended Funds:\n")
print(
    recommended[
        ['scheme_name','risk_grade','sharpe_ratio']
    ]
)