
import pandas as pd
from pathlib import Path

# 1. Load cleaned data
df = pd.read_csv("data/clean_data/sales_data_cleaned.csv")

# 2. Standardize city names to match SQL
df["City"] = df["City"].replace({
    "Ahemdabad": "Ahmedabad",
    "Bangalore": "Bengaluru"
})

# 3. Calculate known gross sales
df["gross_sales"] = df["Quantity"] * df["Unit_Price"]

# 4. Exclude records without a city from city-level grouping
city_data = df.dropna(subset=["City"]).copy()

# 5. Summarize city performance
city_summary = (
    city_data.groupby("City", as_index=False)
    .agg(
        order_count=("Order_ID", "count"),
        units_sold=("Quantity", "sum"),
        missing_price_records=("Unit_Price", lambda x: x.isna().sum()),
        known_gross_sales=("gross_sales", "sum")
    )
    .sort_values("known_gross_sales", ascending=False)
)

# 6. Calculate sales contribution
total_sales = city_summary["known_gross_sales"].sum()

city_summary["sales_share_pct"] = (
    city_summary["known_gross_sales"] / total_sales * 100
).round(2)

# 7. Save report
output_path = Path("reports/city_performance.csv")
city_summary.to_csv(output_path, index=False)

# 8. Display results
print("\nCITY SALES PERFORMANCE")
print(city_summary.to_string(index=False))

print("\nCities analyzed:", len(city_summary))
print("Records without a city:", df["City"].isna().sum())
print("Report saved to:", output_path.resolve())
