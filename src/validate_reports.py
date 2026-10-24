
import pandas as pd
from pathlib import Path

# Reports to validate
files = [
    "reports/category_performance.csv",
    "reports/monthly_performance.csv",
    "reports/city_performance.csv",
    "reports/customer_performance.csv",
    "reports/discount_performance.csv"
]

print("\nREPORT VALIDATION")
print("-" * 70)

# Check that each report exists and can be read
for file in files:
    path = Path(file)

    if not path.exists():
        print(f"MISSING REPORT: {file}")
        continue

    df = pd.read_csv(path)
    print(
        f"{file} | Rows: {len(df)} | Columns: {len(df.columns)}"
    )

# Compare category and monthly sales totals
monthly = pd.read_csv("reports/monthly_performance.csv")
category = pd.read_csv("reports/category_performance.csv")

monthly_total = monthly["known_gross_sales"].sum()
category_total = category["known_gross_sales"].sum()

print("-" * 70)
print(f"Monthly known gross sales: ₹{monthly_total:,.2f}")
print(f"Category known gross sales: ₹{category_total:,.2f}")
print("Totals match:", abs(monthly_total - category_total) < 0.01)

