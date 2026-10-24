
import pandas as pd
from pathlib import Path

# 1. Load cleaned data
df = pd.read_csv("data/clean_data/sales_data_cleaned.csv")

# 2. Calculate known gross sales
df["gross_sales"] = df["Quantity"] * df["Unit_Price"]

# 3. Exclude records with missing customer names
customer_data = df.dropna(subset=["Customer_Name"]).copy()

# 4. Summarize customer performance
customer_summary = (
    customer_data.groupby("Customer_Name", as_index=False)
    .agg(
        order_count=("Order_ID", "count"),
        units_sold=("Quantity", "sum"),
        missing_price_records=("Unit_Price", lambda x: x.isna().sum()),
        known_gross_sales=("gross_sales", "sum")
    )
    .sort_values("known_gross_sales", ascending=False)
)

# 5. Calculate contribution to known gross sales
total_sales = customer_summary["known_gross_sales"].sum()

customer_summary["sales_share_pct"] = (
    customer_summary["known_gross_sales"] / total_sales * 100
).round(2)

# 6. Save the complete customer report
output_path = Path("reports/customer_performance.csv")
customer_summary.to_csv(output_path, index=False)

# 7. Display the top 10 customers
print("\nTOP 10 CUSTOMERS BY KNOWN GROSS SALES")
print(customer_summary.head(10).to_string(index=False))

print("\nUnique customers analyzed:", len(customer_summary))
print("Records with missing customer names:", df["Customer_Name"].isna().sum())
print("Report saved to:", output_path.resolve())
