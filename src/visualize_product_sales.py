
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Load product performance report
df = pd.read_csv("reports/product_performance.csv")

# 2. Select top 10 products and reverse order for horizontal bars
top_products = (
    df.nlargest(10, "known_gross_sales")
    .sort_values("known_gross_sales", ascending=True)
)

# 3. Create output folder
output_dir = Path("reports/charts")
output_dir.mkdir(parents=True, exist_ok=True)

# 4. Create chart
plt.figure(figsize=(11, 7))

bars = plt.barh(
    top_products["Product"],
    top_products["known_gross_sales"] / 100000
)

plt.title("Top 10 Products by Known Gross Sales - 2025")
plt.xlabel("Known Gross Sales (₹ lakh)")
plt.ylabel("Product")

# 5. Add labels
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 1,
        bar.get_y() + bar.get_height() / 2,
        f"₹{width:.1f}L",
        va="center"
    )

# 6. Leave space for labels
plt.xlim(
    0,
    top_products["known_gross_sales"].max() / 100000 * 1.2
)

plt.tight_layout()

# 7. Save and display chart
output_path = output_dir / "top_10_products.png"
plt.savefig(output_path, dpi=300, bbox_inches="tight")
plt.show()

print("Chart saved to:", output_path.resolve())
