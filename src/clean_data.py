
from pathlib import Path
import pandas as pd


# ============================================================
# 1. DEFINE PROJECT PATHS
# ============================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
RAW_FILE = PROJECT_ROOT / "data" / "raw_data" / "sales_data.csv"
OUTPUT_DIR = PROJECT_ROOT / "data" / "clean_data"
OUTPUT_FILE = OUTPUT_DIR / "sales_data_cleaned.csv"


# ============================================================
# 2. LOAD SOURCE DATA
# ============================================================

df = pd.read_csv(RAW_FILE)
original_rows = len(df)

print("\n--- ORIGINAL DATASET ---")
print(f"Source file: {RAW_FILE.name}")
print(f"Original rows: {original_rows}")


# ============================================================
# 3. REMOVE EXACT DUPLICATE ROWS
# ============================================================

# Remove exact duplicates before transforming any values.
exact_duplicates = int(df.duplicated().sum())
df = df.drop_duplicates().copy()

print("\n--- DUPLICATE CLEANING ---")
print(f"Exact duplicate rows removed: {exact_duplicates}")
print(f"Rows remaining: {len(df)}")


# ============================================================
# 4. STANDARDIZE DATE FORMATS
# ============================================================

print("\n--- SAMPLE ORIGINAL DATE VALUES ---")
print(df["Order_Date"].value_counts(dropna=False).head(15))

date_text = df["Order_Date"].astype("string").str.strip()

date_formats = [
    "%Y-%m-%d",
    "%d-%m-%Y",
    "%d/%m/%Y",
    "%d-%b-%Y",
    "%d-%B-%Y",
]

parsed_dates = pd.Series(
    pd.NaT,
    index=df.index,
    dtype="datetime64[ns]"
)

for date_format in date_formats:
    parsed_dates = parsed_dates.fillna(
        pd.to_datetime(
            date_text,
            format=date_format,
            errors="coerce"
        )
    )

unparsed_dates = parsed_dates.isna()

print("\n--- ORIGINAL DATE VALUES THAT COULD NOT BE PARSED ---")

if unparsed_dates.any():
    print(
        df.loc[
            unparsed_dates,
            ["Order_ID", "Order_Date"]
        ].to_string(index=False)
    )
else:
    print("No unparseable date values found.")

df["Order_Date"] = parsed_dates


# ============================================================
# 5. STANDARDIZE CITY TEXT
# ============================================================

df["City"] = df["City"].str.strip().str.title()


# ============================================================
# 6. RESOLVE THE VALIDATED MISSING CITY
# ============================================================

# Assumption: both ORD10212 records represent the same order.
# The matching record supplies Ahmedabad for the missing city.
missing_city_mask = (
    df["Order_ID"].eq("ORD10212")
    & df["City"].isna()
)

resolved_city_count = int(missing_city_mask.sum())
df.loc[missing_city_mask, "City"] = "Ahmedabad"

print("\n--- CITY CLEANING ---")
print(f"Missing cities resolved: {resolved_city_count}")


# 6A. CHECK DUPLICATES AFTER STANDARDIZATION

standardized_duplicates = int(df.duplicated().sum())

print("\n--- DUPLICATES AFTER STANDARDIZATION ---")
print(f"New exact duplicates detected: {standardized_duplicates}")

if standardized_duplicates > 0:
    df = df.drop_duplicates().copy()
    print(f"Rows after removing standardized duplicates: {len(df)}")
else:
    print("No additional exact duplicates found.")

# ============================================================
# 7. CONVERT UNIT PRICE TO NUMERIC
# ============================================================

# Missing prices remain missing; no values are invented.
df["Unit_Price"] = pd.to_numeric(
    df["Unit_Price"],
    errors="coerce"
)


# ============================================================
# 8. INSPECT MISSING UNIT PRICES
# ============================================================

print("\n--- MISSING UNIT PRICE RECORDS ---")

missing_prices = df[df["Unit_Price"].isna()]

print(f"Missing unit prices: {len(missing_prices)}")

if not missing_prices.empty:
    print(
        missing_prices[
            ["Order_ID", "Product", "Quantity", "Unit_Price"]
        ].to_string(index=False)
    )


# ============================================================
# 9. REPORT REMAINING MISSING VALUES
# ============================================================

print("\n--- MISSING VALUES AFTER INITIAL CLEANING ---")
print(df.isnull().sum())

print("\n--- DATA TYPES AFTER INITIAL CLEANING ---")
print(df.dtypes)


# ============================================================
# 10. SAVE CLEANED DATA SEPARATELY
# ============================================================

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

df.to_csv(
    OUTPUT_FILE,
    index=False,
    date_format="%Y-%m-%d"
)

print("\n--- CLEANING SUMMARY ---")
print(f"Original rows: {original_rows}")
print(f"Exact duplicate rows removed: {exact_duplicates}")
print(f"Rows after exact deduplication: {len(df)}")
print(f"Rows removed: {original_rows - len(df)}")
print(f"Cleaned file: {OUTPUT_FILE}")
print("Raw source file was not modified.")
