
from pathlib import Path
import pandas as pd

# 1. Define paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "clean_data" / "sales_data_cleaned.csv"

# 2. Load cleaned data
df = pd.read_csv(DATA_FILE)

print("--- MISSING VALUE SUMMARY ---")
print(df.isnull().sum())

# 3. Inspect records with missing customer names
print("\n--- RECORDS WITH MISSING CUSTOMER NAMES ---")
missing_customers = df[df["Customer_Name"].isna()]

print(
    missing_customers[
        ["Order_ID", "Order_Date", "City", "Category", "Product"]
    ].to_string(index=False)
)

# 4. Inspect records with missing cities
print("\n--- RECORDS WITH MISSING CITIES ---")
missing_cities = df[df["City"].isna()]

print(
    missing_cities[
        ["Order_ID", "Order_Date", "Customer_Name", "Category", "Product"]
    ].to_string(index=False)
)

# 5. Check whether missing customer names or cities repeat
print("\n--- MISSING VALUE COUNTS ---")
print(f"Missing customer names: {df['Customer_Name'].isna().sum()}")
print(f"Missing cities: {df['City'].isna().sum()}")

print("\nInvestigation complete. No records were changed.")

# 6. Inspect records with missing discounts
print("\n--- RECORDS WITH MISSING DISCOUNTS ---")

missing_discounts = df[df["Discount"].isna()]

print(
    missing_discounts[
        [
            "Order_ID",
            "Order_Date",
            "Customer_Name",
            "City",
            "Category",
            "Product",
            "Quantity",
            "Unit_Price",
            "Discount",
        ]
    ].to_string(index=False)
)

print(f"\nMissing discounts: {len(missing_discounts)}")
print("Investigation complete. No records were changed.")

# 7. Validate quantities and unit prices
print("\n--- QUANTITY VALIDATION ---")

print(f"Zero quantities: {(df['Quantity'] == 0).sum()}")
print(f"Negative quantities: {(df['Quantity'] < 0).sum()}")

print("\nRecords with zero or negative quantities:")
print(
    df.loc[
        df["Quantity"] <= 0,
        ["Order_ID", "Product", "Quantity", "Unit_Price", "Discount"]
    ].to_string(index=False)
)

print("\n--- UNIT PRICE VALIDATION ---")

print(f"Missing unit prices: {df['Unit_Price'].isna().sum()}")
print(f"Zero unit prices: {(df['Unit_Price'] == 0).sum()}")
print(f"Negative unit prices: {(df['Unit_Price'] < 0).sum()}")

print("\nRecords with zero or negative unit prices:")
print(
    df.loc[
        df["Unit_Price"].notna() & (df["Unit_Price"] <= 0),
        ["Order_ID", "Product", "Quantity", "Unit_Price"]
    ].to_string(index=False)
)

print("\nValidation complete. No records were changed.")

# 8. Validate discount values
print("\n--- DISCOUNT VALIDATION ---")

valid_discount = df["Discount"].between(0, 100, inclusive="both")

print(f"Missing discounts: {df['Discount'].isna().sum()}")
print(f"Discounts below 0: {(df['Discount'] < 0).sum()}")
print(f"Discounts above 100: {(df['Discount'] > 100).sum()}")

print("\nDiscount values outside 0-100:")
print(
    df.loc[
        df["Discount"].notna() & ~valid_discount,
        ["Order_ID", "Product", "Discount"]
    ].to_string(index=False)
)

print("\nDiscount validation complete. No records were changed.")
