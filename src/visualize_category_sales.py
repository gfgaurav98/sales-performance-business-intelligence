
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Load category report
df = pd.read_csv("reports/category_performance.csv")

# 2. Sort categories by known gross sales
df = df.sort_values("known_gross_sales", ascending=True)

# 3. Create output folder
output_dir = Path("reports/charts")
output_dir.mkdir(parents=True, exist_ok=True)

# 4. Create horizontal bar chart
plt.figure(figsize=(10, 6))

bars = plt.barh(
    df["Category"],
    df["known_gross_sales"] / 100000
)

plt.title("Known Gross Sales by Category - 2025")
plt.xlabel("Known Gross Sales (₹ lakh)")
plt.ylabel("Product Category")

# Display values at the end of each bar
for bar in bars:
    width = bar.get_width()
    plt.text(
        width,
        bar.get_y() + bar.get_height() / 2,
        f" ₹{width:.2f}L",
        va="center",
        ha="left"
    )

plt.tight_layout()

# 5. Save chart
output_path = output_dir / "category_sales.png"
plt.savefig(output_path, dpi=300, bbox_inches="tight")

# 6. Display chart
plt.show()

print("Chart saved to:", output_path.resolve())


