
from pathlib import Path
import pandas as pd

# Locate and load the original dataset
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "raw_data" / "sales_data.csv"

df = pd.read_csv(DATA_FILE)

# 1. Count exact duplicate rows
print("\n--- EXACT DUPLICATE ROWS ---")
print(df.duplicated().sum())

# 2. Display the duplicate rows for inspection
print("\n--- DUPLICATE ROW DETAILS ---")
duplicates = df[df.duplicated(keep=False)]
print(duplicates.sort_values(by="Order_ID").to_string(index=False))

# 3. Check repeated Order_ID values
print("\n--- REPEATED ORDER IDs ---")
repeated_orders = df[
    df.duplicated(subset=["Order_ID"], keep=False)
]

print(repeated_orders.sort_values(by="Order_ID").to_string(index=False))

# 4. Summarize repeated Order_IDs
print("\n--- ORDER ID DUPLICATE COUNTS ---")
print(
    df["Order_ID"]
    .value_counts()
    .loc[lambda counts: counts > 1]
    .sort_index()
)

print("\nInvestigation complete. No records were deleted.")


# 5. Measure order ID uniqueness
print("\n--- ORDER ID SUMMARY ---")
print(f"Total rows: {len(df)}")
print(f"Unique order IDs: {df['Order_ID'].nunique()}")
print(f"Rows with repeated order IDs: {len(repeated_orders)}")

# 6. Count order IDs with conflicting records
print("\n--- REPEATED IDs WITH DIFFERENT RECORDS ---")
distinct_records = (
    repeated_orders.groupby("Order_ID", dropna=False)
    .apply(lambda group: len(group.drop_duplicates()), include_groups=False)
)

conflicting_ids = distinct_records[distinct_records > 1]
print(conflicting_ids)

print(f"Number of IDs with different records: {len(conflicting_ids)}")



# 7. Inspect records that share an Order_ID but differ
print("\n--- CONFLICTING ORDER RECORDS ---")

conflicting_order_ids = ["ORD10132", "ORD10212", "ORD10907"]

conflict_details = df[
    df["Order_ID"].isin(conflicting_order_ids)
].sort_values("Order_ID")

print(conflict_details.to_string(index=False))


# 8. Validate proposed cleaning decisions
print("\n--- PROPOSED CLEANING VALIDATION ---")

# Check whether ORD10132 has equivalent dates
dates_10132 = df.loc[
    df["Order_ID"] == "ORD10132", "Order_Date"
]
parsed_dates_10132 = pd.to_datetime(
    dates_10132, dayfirst=True, errors="coerce"
)
print(
    "ORD10132 dates equivalent:",
    parsed_dates_10132.nunique() == 1
)

# Check whether ORD10212 differs only in City
records_10212 = df[df["Order_ID"] == "ORD10212"]
print(
    "\nORD10212 matching fields:",
    records_10212.drop(columns=["City"]).nunique().to_dict()
)

print("\nORD10212 city values:")
print(records_10212["City"].tolist())

# Check city formatting for ORD10907
records_10907 = df[df["Order_ID"] == "ORD10907"]
normalized_cities = records_10907["City"].str.strip().str.casefold()
print(
    "\nORD10907 cities equivalent after normalization:",
    normalized_cities.nunique() == 1
)

