
from pathlib import Path

import pandas as pd
import numpy as np

# 1. Locate and load the cleaned dataset
PROJECT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = PROJECT_DIR / "data" / "clean_data" / "sales_data_cleaned.csv"

df = pd.read_csv(DATA_PATH)
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# 2. Dataset overview
print("\n=== DATASET OVERVIEW ===")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")
print(f"Date range: {df['Order_Date'].min()} to {df['Order_Date'].max()}")

# 3. Data types
print("\n=== DATA TYPES ===")
print(df.dtypes)

# 4. Missing values
print("\n=== MISSING VALUES ===")
missing = df.isna().sum()
missing_report = pd.DataFrame({
    "missing_count": missing,
    "missing_pct": (missing / len(df) * 100).round(2),
})
print(missing_report[missing_report["missing_count"] > 0])

# 5. Numeric summary
print("\n=== NUMERIC SUMMARY ===")
print(df[["Quantity", "Unit_Price", "Discount"]].describe().round(2))

# 6. Data-quality checks
print("\n=== DATA QUALITY CHECKS ===")
print(f"Duplicate rows: {df.duplicated().sum()}")
print(f"Duplicate order IDs: {df['Order_ID'].duplicated().sum()}")
print(f"Nonpositive quantities: {(df['Quantity'] <= 0).sum()}")
print(f"Nonpositive unit prices: {(df['Unit_Price'].dropna() <= 0).sum()}")
print(f"Discounts outside 0-100: {((df['Discount'] < 0) | (df['Discount'] > 100)).sum()}")

# 7. Provisional gross sales
# Missing prices are excluded; discounts are not applied.
df["Gross_Sales"] = df["Quantity"] * df["Unit_Price"]

print("\n=== PROVISIONAL GROSS SALES ===")
print(f"Known gross sales: ₹{df['Gross_Sales'].sum(skipna=True):,.2f}")
print(f"Records with missing unit prices: {df['Unit_Price'].isna().sum()}")
print(f"Units with missing unit prices: {df.loc[df['Unit_Price'].isna(), 'Quantity'].sum()}")

# 8. Category summary
category_summary = (
    df.groupby("Category", dropna=False)
    .agg(
        order_count=("Order_ID", "count"),
        units_sold=("Quantity", "sum"),
        known_gross_sales=("Gross_Sales", "sum"),
    )
    .sort_values("known_gross_sales", ascending=False)
)

print("\n=== CATEGORY PERFORMANCE ===")
print(category_summary.round(2).to_string())

# 9. Monthly summary
monthly_summary = (
    df.groupby(df["Order_Date"].dt.month)
    .agg(
        order_count=("Order_ID", "count"),
        known_gross_sales=("Gross_Sales", "sum"),
    )
    .rename_axis("month_number")
)

print("\n=== MONTHLY PERFORMANCE ===")
print(monthly_summary.round(2).to_string())
