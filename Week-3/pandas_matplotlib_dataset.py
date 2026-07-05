"""
Week 3 - Thursday
Topic: Pandas + Matplotlib - visualise a real-style dataset

Note: this uses a synthetic dataset generated locally instead of a live
Kaggle download, so the script runs anywhere without an internet
connection or an API key. Swap `generate_dataset()` for
`pd.read_csv("your_kaggle_file.csv")` to use a real Kaggle CSV -
everything after that point works the same way.

Covers:
- Loading tabular data into pandas
- Grouping + aggregating for a chart-ready summary
- Bar chart, line chart, histogram, scatter plot with matplotlib
- Saving each figure to disk
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def generate_dataset(n=200, seed=42):
    """Simulate a student study-hours-vs-score dataset (Kaggle-style CSV)."""
    rng = np.random.default_rng(seed)
    cities = ["Hyderabad", "Chennai", "Bangalore", "Pune"]
    city = rng.choice(cities, size=n)
    study_hours = rng.uniform(1, 8, size=n).round(1)
    # score roughly follows study hours + noise, capped at 100
    score = np.clip(40 + study_hours * 7 + rng.normal(0, 8, size=n), 0, 100).round(1)
    return pd.DataFrame({"city": city, "study_hours": study_hours, "score": score})


df = generate_dataset()
print("Dataset preview:")
print(df.head())
print("\nShape:", df.shape)

# ---------------------------------------------------------------------
# 1. Bar chart - average score per city
# ---------------------------------------------------------------------
avg_score_by_city = df.groupby("city")["score"].mean().sort_values(ascending=False)
print("\nAverage score by city:")
print(avg_score_by_city)

plt.figure(figsize=(6, 4))
avg_score_by_city.plot(kind="bar", color="steelblue")
plt.title("Average Score by City")
plt.ylabel("Average Score")
plt.xlabel("City")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("chart_bar_avg_score_by_city.png", dpi=120)
plt.close()

# ---------------------------------------------------------------------
# 2. Histogram - distribution of scores
# ---------------------------------------------------------------------
plt.figure(figsize=(6, 4))
plt.hist(df["score"], bins=15, color="seagreen", edgecolor="black")
plt.title("Distribution of Scores")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("chart_hist_scores.png", dpi=120)
plt.close()

# ---------------------------------------------------------------------
# 3. Scatter plot - study hours vs score, with trend line
# ---------------------------------------------------------------------
slope, intercept = np.polyfit(df["study_hours"], df["score"], 1)
trend_x = np.linspace(df["study_hours"].min(), df["study_hours"].max(), 100)
trend_y = slope * trend_x + intercept

plt.figure(figsize=(6, 4))
plt.scatter(df["study_hours"], df["score"], alpha=0.6, label="Students")
plt.plot(trend_x, trend_y, color="red", label=f"Trend (slope={slope:.1f})")
plt.title("Study Hours vs Score")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.legend()
plt.tight_layout()
plt.savefig("chart_scatter_hours_vs_score.png", dpi=120)
plt.close()

# ---------------------------------------------------------------------
# 4. Line chart - rolling average score sorted by study hours
# ---------------------------------------------------------------------
sorted_df = df.sort_values("study_hours").reset_index(drop=True)
sorted_df["rolling_score"] = sorted_df["score"].rolling(window=15, min_periods=1).mean()

plt.figure(figsize=(6, 4))
plt.plot(sorted_df["study_hours"], sorted_df["rolling_score"], color="darkorange")
plt.title("Rolling Average Score vs Study Hours")
plt.xlabel("Study Hours (sorted)")
plt.ylabel("Rolling Average Score")
plt.tight_layout()
plt.savefig("chart_line_rolling_avg.png", dpi=120)
plt.close()

print("\nSaved 4 charts: bar, histogram, scatter, line.")
print(f"Correlation between study hours and score: {df['study_hours'].corr(df['score']):.2f}")