# Quantity Outlier Review

## Project
Sales Performance & Business Intelligence

## Method
The Interquartile Range (IQR) method was used to flag unusually high quantities.

- Q1: 2 units
- Q3: 5 units
- IQR: 3 units
- Upper threshold: 9.5 units
- Flagging rule: Quantity > 9.5

## Results
- Potential outlier records: 22
- Three records have quantities of 75 units.
- One record has a quantity of 50 units.
- Eighteen records have quantities of 10 units.

## Initial Assessment
The records with quantities of 50 and 75 require further review.
Orders of 10 units may represent legitimate bulk purchases.

## Decision
No records were deleted or modified.
The IQR rule identifies statistical outliers, not confirmed data errors.
Business validation is required before excluding or correcting any record.

## Next Actions
1. Confirm whether bulk orders are valid in this dataset.
2. Check the source records for the four highest quantities.
3. Keep all records unless a business rule or source evidence supports a change.
