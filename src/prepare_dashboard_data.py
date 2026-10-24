
import pandas as pd
from pathlib import Path

# 1. Load cleaned data
df = pd.read_csv("data/clean_data/sales_data_cleaned.csv")

# 2. Parse order dates
df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# 3. Standardize city names to match SQL analysis
df["City"] = df["City"].replace({
    "Ahemdabad": "Ahmedabad",
    "Bangalore": "Bengaluru"
})

# 4. Add time dimensions for Power BI
df["Year"] = df["Order_Date"].dt.year
df["Month_Number"] = df["Order_Date"].dt.month
df["Month_Name"] = df["Order_Date"].dt.strftime("%B")
df["Quarter"] = "Q" + df["Order_Date"].dt.quarter.astype(str)

# 5. Calculate known gross sales
# Missing unit prices remain missing; they are not treated as zero.
df["Known_Gross_Sales"] = df["Quantity"] * df["Unit_Price"]

# 6. Create Power BI export folder
output_dir = Path("data/powerbi")
output_dir.mkdir(parents=True, exist_ok=True)

# 7. Export dashboard dataset
output_path = output_dir / "sales_dashboard_data.csv"
df.to_csv(output_path, index=False)

# 8. Verify export
check = pd.read_csv(output_path)

print("\nDASHBOARD DATA EXPORT")
print("Rows:", len(check))
print("Columns:", len(check.columns))
print("Missing unit prices:", check["Unit_Price"].isna().sum())
print("Missing cities:", check["City"].isna().sum())
print("Missing customer names:", check["Customer_Name"].isna().sum())
print("Export saved to:", output_path.resolve())

