
import getpass
from pathlib import Path

import mysql.connector
import pandas as pd

PROJECT_DIR = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_DIR / "data" / "clean_data" / "sales_data_cleaned.csv"

# Load CSV and convert missing values to Python None (SQL NULL)
df = pd.read_csv(CSV_PATH, dtype={"Order_ID": str})
df = df.astype(object).where(pd.notna(df), None)

columns = [
    "Order_ID", "Order_Date", "Customer_Name", "City",
    "Category", "Product", "Quantity", "Unit_Price", "Discount"
]

records = list(df[columns].itertuples(index=False, name=None))

print(f"CSV records to import: {len(records)}")

password = getpass.getpass("Enter your MySQL password: ")

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=password,
    database="sales_performance",
)

try:
    cursor = connection.cursor()

    # Prevent accidental duplicate imports
    cursor.execute("SELECT COUNT(*) FROM sales")
    existing_rows = cursor.fetchone()[0]

    if existing_rows > 0:
        raise RuntimeError(
            f"The sales table already contains {existing_rows} rows. "
            "Import stopped to prevent duplicate data."
        )

    insert_sql = """
        INSERT INTO sales (
            Order_ID, Order_Date, Customer_Name, City,
            Category, Product, Quantity, Unit_Price, Discount
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    cursor.executemany(insert_sql, records)
    connection.commit()

    cursor.execute("SELECT COUNT(*) FROM sales")
    total_rows = cursor.fetchone()[0]

    print(f"Rows inserted: {cursor.rowcount}")
    print(f"Total rows in MySQL: {total_rows}")

except Exception:
    connection.rollback()
    raise

finally:
    if "cursor" in locals():
        cursor.close()
    connection.close()
