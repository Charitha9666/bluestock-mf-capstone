# Bluestock Mutual Fund Analytics Platform

## Project Overview

The Bluestock Mutual Fund Analytics Platform is a data analytics project designed to evaluate mutual fund performance, investor behavior, portfolio diversification, and SIP continuity. The project leverages Python, SQL, and data visualization techniques to generate meaningful insights and support investment decision-making.

---

## Key Features

- Automated ETL (Extract, Transform, Load) Pipeline
- Mutual Fund Performance Analysis
- Risk Analysis using VaR, CVaR, and Sharpe Ratio
- Investor Cohort Analysis
- SIP Continuity Assessment
- Portfolio Diversification Analysis using HHI
- Fund Recommendation System
- Data Visualization and Reporting

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- SQL
- Jupyter Notebook
- Visual Studio Code

---

## Project Structure

```text
bluestock_mf_capstone/
│
├── data/
├── notebooks/
├── reports/
├── scripts/
├── sql/
├── README.md
└── requirements.txt
```

---

## Generated Reports

The project generates the following analytical outputs:

- var_cvar_report.csv
- cohort_analysis.csv
- sip_continuity.csv
- sector_hhi.csv
- rolling_sharpe_chart.png

---

## Fund Recommendation Module

The recommendation engine filters mutual funds based on the selected risk profile and ranks them using the Sharpe Ratio to suggest suitable investment options.

Supported Risk Levels:

- Low
- Moderate
- High

---

## How to Run the Project

```bash
python run_pipeline.py
```

---

## Key Insights

- Small-cap funds exhibit higher downside risk based on VaR and CVaR metrics.
- Funds with higher Sharpe Ratios provide better risk-adjusted returns.
- Recent investor cohorts contribute significantly to overall investments.
- SIP continuity analysis helps identify at-risk investors.
- HHI analysis reveals the level of portfolio concentration across funds.

---

## Author

**Gurram Sai Sree Charitha**

Capstone Project – Mutual Fund Analytics Platform