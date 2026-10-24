# Data Quality Report
## Project: Sales Performance & Business Intelligence

### 1. Dataset Overview
- Source file: `sales_data.csv`
- Original records: 1,000
- Cleaned records: 988
- Columns: 9
- Analysis period: 2025
- Tools: Python and Pandas

### 2. Cleaning Results

| Check | Result | Treatment |
|---|---|---|
| Exact duplicate rows in source | 9 | Removed |
| Additional duplicates after standardization | 3 | Removed from the working dataset |
| Remaining exact duplicates | 0 | Verified after saving |
| Date formats | Multiple formats | Standardized to `YYYY-MM-DD` |
| Unparseable dates | 0 | All dates parsed successfully |
| Missing customer names | 10 | Retained as missing |
| Missing cities | 17 | Retained as missing, except the validated `ORD10212` resolution |
| Missing unit prices | 12 | Retained as missing |
| Missing discounts | 15 | Retained as missing |
| Zero quantities | 1 | Flagged for business review |
| Negative quantities | 0 | None detected |
| Negative unit prices | 0 | None detected among non-missing values |
| Discounts outside 0–100 | 0 | None detected |

### 3. Business Assumptions
- The raw dataset remains unchanged.
- Exact duplicate records are removed from the working dataset.
- Three additional rows became exact duplicates after standardization and were removed.
- The missing city for `ORD10212` was resolved to Ahmedabad based on a matching record, assuming both rows represent the same order.
- Missing prices, discounts, and customer names were not guessed or filled.
- The zero-quantity record `ORD10549` remains flagged for business review.
- The meaning of `Discount` must be confirmed before calculating net sales.

### 4. Outstanding Actions
1. Review the three records removed after standardization and document the matching rule.
2. Investigate the 12 missing unit prices.
3. Confirm the business meaning of discounts and how missing discounts should be treated.
4. Confirm how zero-quantity orders should affect sales KPIs.
5. Define revenue and order-count calculations.
6. Validate the analytical dataset before final reporting.

### 5. Current Status
Initial profiling, duplicate handling, date standardization, and numeric validation are complete. The working dataset contains 988 records and no exact duplicate rows. It is not yet approved for final KPI reporting because some data-quality issues and business definitions remain unresolved.
