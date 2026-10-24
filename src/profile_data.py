
from pathlib import Path
import pandas as pd

# 1. Define the project paths
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_FILE = PROJECT_ROOT / "data" / "raw_data" / "sales_data.csv"

# 2. Load the raw dataset
df = pd.read_csv(DATA_FILE)

# 3. Display the initial data profile
print("\n--- DATASET OVERVIEW ---")
print(f"File: {DATA_FILE.name}")
print(f"Rows: {df.shape[0]}")
print(f"Columns: {df.shape[1]}")

print("\n--- COLUMN NAMES ---")
print(df.columns.tolist())

print("\n--- DATA TYPES ---")
print(df.dtypes)

print("\n--- MISSING VALUES ---")
print(df.isnull().sum())

print("\n--- EXACT DUPLICATE ROWS ---")
print(df.duplicated().sum())

print("\n--- SAMPLE RECORDS ---")
print(df.head())

print("\n--- NUMERIC SUMMARY ---")
print(df.describe())
