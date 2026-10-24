
import pandas as pd
from pathlib import Path

# 1. Load cleaned data
df = pd.read_csv("data/clean_data/sales_data_cleaned.csv")

# 2. Calculate known gross sales before discounts
df["gross_sales"] = df["Quantity"] * df["Unit_Price"]

# 3. Group recorded discounts into bands
bins = [0, 5, 10, 15, 20, 25]
labels = ["0 to <5", "5 to <10", "10 to <15", "15 to <20", "20 to 25"]

df["discount_band"] = pd.cut(
    df["Discount"],
    bins=bins,
    labels=labels,
    right=False,
    include_lowest=True
)

# 4. Label missing discounts separately
df["discount_band"] = df["discount_band"].astype("object")
df.loc[df["Discount"].isna(), "discount_band"] = "Missing"

# 5. Summarize recorded discount bands
discount_summary = (
    df.groupby("discount_band", observed=False, dropna=False)
    .agg(
        order_count=("Order_ID", "count"),
        units_sold=("Quantity", "sum"),
        known_gross_sales=("gross_sales", "sum"),
        missing_price_records=("Unit_Price", lambda x: x.isna().sum())
    )
    .reset_index()
)

# 6. Calculate contribution to known gross sales
total_sales = discount_summary["known_gross_sales"].sum()

discount_summary["sales_share_pct"] = (
    discount_summary["known_gross_sales"] / total_sales * 100
).round(2)

# 7. Save report
output_path = Path("reports/discount_performance.csv")
discount_summary.to_csv(output_path, index=False)

# 8. Display results
print("\nDISCOUNT BAND ANALYSIS")
print(discount_summary.to_string(index=False))

print("\nMissing discount values:", df["Discount"].isna().sum())
print("Report saved to:", output_path.resolve())

