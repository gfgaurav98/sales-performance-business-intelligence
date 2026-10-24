# Sales Performance & Business Intelligence

## Project Overview

An end-to-end sales analytics project designed to evaluate sales performance across products, categories, cities, customers, and months. The project follows a structured analytics workflow, from data profiling and cleaning through SQL analysis, Python reporting, and Power BI visualization.

**Business objective:** Identify sales trends, understand category and product contributions, compare city performance, and produce actionable insights for business decision-making.

## Technology Stack

- **SQL:** MySQL 8 — querying, aggregation, business analysis, and data-quality validation
- **Python:** Pandas, NumPy, Matplotlib — data cleaning, exploratory analysis, reporting, and visualization
- **Power BI:** Interactive dashboard, KPI cards, slicers, and DAX measures
- **Development tools:** Cursor IDE, PowerShell, Git
- **Data formats:** CSV, SQL, PNG, PBIX, Markdown

## Dataset Overview

| Attribute | Details |
|---|---|
| Original records | 1,000 |
| Cleaned records | 988 |
| Columns | 9 original fields |
| Analysis period | January–December 2025 |
| Distinct named customers | 10 |
| Distinct products | 20 |
| Standardized cities | 12 |

The dataset contains order dates, customer names, cities, product categories, products, quantities, unit prices, and discount values.

## Project Workflow

### 1. Data Profiling and Quality Assessment
- Examined dataset structure, column types, missing values, and duplicate records.
- Investigated repeated order IDs and date-format inconsistencies.
- Identified zero-quantity records and potential quantity outliers.
- Documented data-quality findings and cleaning decisions.

### 2. Data Cleaning
- Removed duplicate records according to documented cleaning rules.
- Standardized date formats and city names.
- Preserved unresolved missing values for transparent reporting.
- Retained potential quantity outliers pending business validation.
- Preserved the original raw dataset.

### 3. SQL Analysis
Used MySQL to analyze:
- Sales by product category
- Monthly sales trends
- Top-performing products
- City-level sales performance
- Customer contributions
- Sales across recorded discount bands
- Data quality and missing values

### 4. Python Analysis
Developed reusable scripts for:
- Exploratory data analysis
- Category performance
- Monthly performance
- City performance
- Customer performance
- Product performance
- Discount-band analysis
- KPI summary generation
- Report validation and chart creation

### 5. Power BI Dashboard
Built an interactive report featuring:
- Known Gross Sales KPI
- Total Units Sold KPI
- Month and Category slicers
- Monthly sales trend
- Sales by category
- Sales by city
- Top-products analysis

## Key Findings

| Metric | Result |
|---|---:|
| Cleaned records | 988 |
| Known gross sales | ₹6,22,20,420 |
| Units recorded | 4,108 |
| Highest-sales month | May |
| Highest-sales category | Home Appliances |
| Highest-sales city | Noida |
| Highest-sales product | Washing Machine |

Additional findings:
- Home Appliances and Electronics are the leading categories by known gross sales.
- May recorded the highest monthly sales, while March recorded the lowest.
- Noida led the city comparison, followed by Jaipur.
- Washing Machines ranked first among products by known gross sales.

## Data Quality and Limitations

- 12 records have missing unit prices.
- 17 records have missing city values.
- 10 records have missing customer names.
- 15 records have missing discount values.
- One record has zero quantity.
- 22 records were flagged for potential quantity outliers and retained for review.
- Discount semantics have not been confirmed.

**Metric definition:** Known gross sales is calculated as `Quantity × Unit_Price`, summed across records with available unit prices. It is a pre-discount measure, not confirmed net revenue or profit. Totals may exclude sales associated with missing prices.

## Repository Structure

```text
Sales-Performance-Business-Intelligence/
├── data/
│   ├── raw_data/
│   ├── clean_data/
│   └── powerbi/
├── reports/
│   ├── charts/
│   ├── category_performance.csv
│   ├── city_performance.csv
│   ├── customer_performance.csv
│   ├── discount_performance.csv
│   ├── kpi_summary.csv
│   ├── monthly_performance.csv
│   ├── product_performance.csv
│   ├── data_quality_report.md
│   └── quantity_outlier_review.md
├── sql/
│   └── sales_analysis.sql
├── src/
│   ├── clean_data.py
│   ├── exploratory_analysis.py
│   ├── category_analysis.py
│   ├── monthly_analysis.py
│   ├── city_analysis.py
│   ├── customer_analysis.py
│   ├── product_analysis.py
│   ├── discount_analysis.py
│   ├── kpi_summary.py
│   └── validate_reports.py
├── Sales_Performance_Business_Intelligence.pbix
└── README.md
```

## How to Reproduce the Analysis

1. Install Python and create a virtual environment.
2. Install the required libraries: Pandas, NumPy, and Matplotlib.
3. Place the authorized source dataset in `data/raw_data/`.
4. Run the profiling and cleaning scripts in `src/`.
5. Create the MySQL database and table, then import the cleaned data.
6. Execute the queries in `sql/sales_analysis.sql`.
7. Run the Python analysis scripts to generate reports and charts.
8. Open the `.pbix` file in Power BI Desktop to explore the dashboard.

Database credentials should be supplied securely and must not be committed to source control.

## Business Value

This project demonstrates how raw sales data can be transformed into validated datasets, reproducible analysis, documented findings, and interactive business reporting. It showcases practical skills in SQL, Python, data quality, KPI development, visualization, and business interpretation.

## Author

**Gaurav Fegade**

Data Analytics Portfolio Project
