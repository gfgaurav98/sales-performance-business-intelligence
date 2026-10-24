
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Load city performance report
df = pd.read_csv("reports/city_performance.csv")

# 2. Sort cities from lowest to highest sales
df = df.sort_values("known_gross_sales", ascending=True)

# 3. Create output folder
output_dir = Path("reports/charts")
output_dir.mkdir(parents=True, exist_ok=True)

# 4. Create horizontal bar chart
plt.figure(figsize=(11, 7))

bars = plt.barh(
    df["City"],
    df["known_gross_sales"] / 100000
)

plt.title("Known Gross Sales by City - 2025")
plt.xlabel("Known Gross Sales (₹ lakh)")
plt.ylabel("City")

# 5. Add sales values to the bars
for bar in bars:
    width = bar.get_width()
    plt.text(
        width + 2,
        bar.get_y() + bar.get_height() / 2,
        f"₹{width:.1f}L",
        va="center"
    )

# Leave space for value labels
plt.xlim(0, df["known_gross_sales"].max() / 100000 * 1.18)
plt.tight_layout()

# 6. Save chart
output_path = output_dir / "city_sales.png"
plt.savefig(output_path, dpi=300, bbox_inches="tight")

# 7. Display chart
plt.show()

print("Chart saved to:", output_path.resolve())

