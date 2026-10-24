
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# 1. Load monthly performance report
df = pd.read_csv("reports/monthly_performance.csv")

# 2. Create output folder
output_dir = Path("reports/charts")
output_dir.mkdir(parents=True, exist_ok=True)

# 3. Create the chart
plt.figure(figsize=(12, 6))

plt.plot(
    df["Month_Name"],
    df["known_gross_sales"] / 100000,
    marker="o",
    linewidth=2
)

plt.title("Monthly Sales Performance - 2025")
plt.xlabel("Month")
plt.ylabel("Known Gross Sales (₹ lakh)")
plt.xticks(rotation=45)
plt.grid(True, linestyle="--", alpha=0.4)
plt.tight_layout()

# 4. Save chart as an image
output_path = output_dir / "monthly_sales_trend.png"
plt.savefig(output_path, dpi=300, bbox_inches="tight")

# 5. Display chart
plt.show()

print("Chart saved to:", output_path.resolve())
