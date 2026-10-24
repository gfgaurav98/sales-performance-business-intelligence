
import pandas as pd
from pathlib import Path

# 1. Load cleaned data
df = pd.read_csv("data/clean_data/sales_data_cleaned.csv")

# 2. Calculate known gross sales before discounts
df["gross_sales"] = df["Quantity"] * df["Unit_Price"]

# 3. Summarize product performance
product_summary = (
    df.groupby("Product", as_index=False)
    .agg(
        order_count=("Order_ID", "count"),
        units_sold=("Quantity", "sum"),
        missing_price_records=("Unit_Price", lambda x: x.isna().sum()),
        known_gross_sales=("gross_sales", "sum")
    )
    .sort_values("known_gross_sales", ascending=False)
)

# 4. Calculate contribution to known gross sales
total_sales = product_summary["known_gross_sales"].sum()

product_summary["sales_share_pct"] = (
    product_summary["known_gross_sales"] / total_sales * 100
).round(2)

# 5. Save complete product report
output_path = Path("reports/product_performance.csv")
product_summary.to_csv(output_path, index=False)

# 6. Display top 10 products
print("\nTOP 10 PRODUCTS BY KNOWN GROSS SALES")
print(product_summary.head(10).to_string(index=False))

print("\nUnique products analyzed:", len(product_summary))
print("Report saved to:", output_path.resolve())

