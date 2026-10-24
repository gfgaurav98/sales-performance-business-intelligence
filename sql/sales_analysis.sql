-- Project: Sales Performance & Business Intelligence
-- Analysis: Gross sales and units sold by category
-- Note: Gross sales are before discounts and exclude missing unit prices.

USE sales_performance;

SELECT
    Category,
    COUNT(*) AS order_count,
    SUM(Quantity) AS units_sold,
    ROUND(SUM(Quantity * Unit_Price), 2) AS known_gross_sales
FROM sales
GROUP BY Category
ORDER BY known_gross_sales DESC;

-- Analysis: Monthly sales trend
-- Purpose: Identify high- and low-performing months.
-- Note: Gross sales are before discounts and exclude missing unit prices.

SELECT
    MONTH(Order_Date) AS month_number,
    DATE_FORMAT(Order_Date, '%b') AS month,
    COUNT(*) AS order_count,
    ROUND(SUM(Quantity * Unit_Price), 2) AS known_gross_sales
FROM sales
GROUP BY MONTH(Order_Date), DATE_FORMAT(Order_Date, '%b')
ORDER BY month_number;

-- Analysis: Top 10 products by known gross sales
-- Purpose: Identify products contributing the most gross sales.
-- Note: Gross sales are before discounts and exclude missing unit prices.

SELECT
    Product,
    Category,
    SUM(Quantity) AS units_sold,
    COUNT(*) AS order_count,
    ROUND(SUM(Quantity * Unit_Price), 2) AS known_gross_sales
FROM sales
GROUP BY Product, Category
ORDER BY known_gross_sales DESC
LIMIT 10;

-- Analysis: Sales performance by city
-- Purpose: Compare geographic sales performance.
-- Note: Missing cities are excluded; gross sales are before discounts.

SELECT
    City,
    COUNT(*) AS order_count,
    SUM(Quantity) AS units_sold,
    ROUND(SUM(Quantity * Unit_Price), 2) AS known_gross_sales
FROM sales
WHERE City IS NOT NULL
GROUP BY City
ORDER BY known_gross_sales DESC;

-- Analysis: Top 10 customers by known gross sales
-- Purpose: Identify customers contributing the most gross sales.
-- Note: Customers with missing names are excluded.

SELECT
    Customer_Name,
    COUNT(*) AS order_count,
    SUM(Quantity) AS units_sold,
    ROUND(SUM(Quantity * Unit_Price), 2) AS known_gross_sales
FROM sales
WHERE Customer_Name IS NOT NULL
GROUP BY Customer_Name
ORDER BY known_gross_sales DESC
LIMIT 10;

-- Analysis: Gross sales by discount band
-- Purpose: Compare sales across observed discount ranges.
-- Note: Discount meaning is not yet confirmed; this does not calculate net sales.

SELECT
    CASE
        WHEN Discount IS NULL THEN 'Missing'
        WHEN Discount < 5 THEN '0 to <5'
        WHEN Discount < 10 THEN '5 to <10'
        WHEN Discount < 15 THEN '10 to <15'
        WHEN Discount < 20 THEN '15 to <20'
        ELSE '20 to 25'
    END AS discount_band,
    COUNT(*) AS order_count,
    ROUND(SUM(Quantity * Unit_Price), 2) AS known_gross_sales
FROM sales
GROUP BY discount_band
ORDER BY MIN(Discount);

-- Analysis: Data-quality validation
-- Purpose: Identify missing and invalid values before reporting.

SELECT
    COUNT(*) AS total_records,
    COUNT(DISTINCT Order_ID) AS unique_order_ids,
    SUM(Order_ID IS NULL) AS missing_order_ids,
    SUM(Order_Date IS NULL) AS missing_dates,
    SUM(Customer_Name IS NULL) AS missing_customers,
    SUM(City IS NULL) AS missing_cities,
    SUM(Quantity IS NULL) AS missing_quantities,
    SUM(Quantity <= 0) AS nonpositive_quantities,
    SUM(Unit_Price IS NULL) AS missing_prices,
    SUM(Unit_Price <= 0) AS nonpositive_prices,
    SUM(Discount IS NULL) AS missing_discounts
FROM sales;

