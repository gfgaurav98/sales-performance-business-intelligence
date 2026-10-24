
from pathlib import Path
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "clean_data" / "sales_data_cleaned.csv"
OUTPUT_PATH = PROJECT_DIR / "reports" / "category_performance.csv"

df = pd.read_csv(DATA_PATH)

# Gross sales are calculated before discounts.
# Missing unit prices remain missing and are excluded from the sum.
df["Gross_Sales"] = df["Quantity"] * df["Unit_Price"]

category_summary = (
    df.groupby("Category")
    .agg(
        order_count=("Order_ID", "count"),
        units_sold=("Quantity", "sum"),
        missing_price_records=("Unit_Price", lambda s: s.isna().sum()),
        known_gross_sales=("Gross_Sales", "sum"),
    )
    .reset_index()
)

total_known_gross_sales = category_summary["known_gross_sales"].sum()

category_summary["sales_share_pct"] = (
    category_summary["known_gross_sales"]
    / total_known_gross_sales
    * 100
).round(2)

category_summary = category_summary.sort_values(
    "known_gross_sales", ascending=False
)

OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
category_summary.to_csv(OUTPUT_PATH, index=False)

print("=== CATEGORY PERFORMANCE ===")
print(category_summary.round(2).to_string(index=False))
print(f"\nReport saved to: {OUTPUT_PATH}")
