
import pandas as pd
from pathlib import Path

# Load cleaned data
df = pd.read_csv("data/clean_data/sales_data_cleaned.csv")

# Calculate known gross sales before discounts
df["gross_sales"] = df["Quantity"] * df["Unit_Price"]

# Load category and monthly reports
category = pd.read_csv("reports/category_performance.csv")
monthly = pd.read_csv("reports/monthly_performance.csv")
city = pd.read_csv("reports/city_performance.csv")
product = pd.read_csv("reports/product_performance.csv")

# Calculate headline KPIs
kpis = {
    "total_records": len(df),
    "unique_customers": df["Customer_Name"].nunique(),
    "unique_products": df["Product"].nunique(),
    "cities_with_sales": df["City"].replace({
    "Ahemdabad": "Ahmedabad",
    "Bangalore": "Bengaluru"
}).nunique(),
    "total_units_sold": df["Quantity"].sum(),
    "known_gross_sales": df["gross_sales"].sum(),
    "missing_price_records": int(df["Unit_Price"].isna().sum()),
    "missing_city_records": int(df["City"].isna().sum()),
    "missing_customer_records": int(df["Customer_Name"].isna().sum()),
    "best_sales_month": monthly.loc[
        monthly["known_gross_sales"].idxmax(), "Month_Name"
    ],
    "best_sales_category": category.loc[
        category["known_gross_sales"].idxmax(), "Category"
    ],
    "top_sales_city": city.loc[
        city["known_gross_sales"].idxmax(), "City"
    ],
    "top_sales_product": product.loc[
        product["known_gross_sales"].idxmax(), "Product"
    ],
}

# Save KPI report
kpi_report = pd.DataFrame(
    [{"KPI": key, "Value": value} for key, value in kpis.items()]
)

output_path = Path("reports/kpi_summary.csv")
kpi_report.to_csv(output_path, index=False)

# Display KPI results
print("\nBUSINESS KPI SUMMARY")
print(kpi_report.to_string(index=False))
print("\nReport saved to:", output_path.resolve())
