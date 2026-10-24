
import pandas as pd
from pathlib import Path

# 1. Load the cleaned dataset
df = pd.read_csv("data/clean_data/sales_data_cleaned.csv")

# 2. Convert Order_Date to a proper date format
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# 3. Calculate known gross sales
# Rows with missing prices are excluded from the revenue calculation
df["gross_sales"] = df["Quantity"] * df["Unit_Price"]

# 4. Extract month from the order date
df["Month"] = df["Order_Date"].dt.month
df["Month_Name"] = df["Order_Date"].dt.strftime("%B")

# 5. Summarize monthly performance
monthly = (
    df.groupby(["Month", "Month_Name"], as_index=False)
    .agg(
        order_count=("Order_ID", "count"),
        units_sold=("Quantity", "sum"),
        missing_price_records=("Unit_Price", lambda x: x.isna().sum()),
        known_gross_sales=("gross_sales", "sum")
    )
    .sort_values("Month")
)

# 6. Calculate each month's share of known gross sales
total_sales = monthly["known_gross_sales"].sum()

monthly["sales_share_pct"] = (
    monthly["known_gross_sales"] / total_sales * 100
).round(2)

# 7. Save the report
output_path = Path("reports/monthly_performance.csv")
monthly.to_csv(output_path, index=False)

# 8. Display results
print("\nMONTHLY SALES PERFORMANCE")
print(monthly.to_string(index=False))

print("\nTotal months:", len(monthly))
print("Total known gross sales: ₹{:,.2f}".format(total_sales))
print("Report saved to:", output_path.resolve())

