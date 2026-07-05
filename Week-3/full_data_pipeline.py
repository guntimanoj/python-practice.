"""
Week 3 - Friday
Topic: Full data analysis pipeline (load -> clean -> analyse -> visualise -> report)

This ties together everything from Mon-Thu into one end-to-end pipeline,
the way a real Kaggle notebook or work project would be structured.

Pipeline stages:
1. Load raw data (with some messiness baked in on purpose)
2. Clean (handle missing values, fix types, drop duplicates)
3. Analyse (groupby summaries, correlations)
4. Visualise (save charts)
5. Report (print a short written summary of findings)
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------
# 1. LOAD - simulate a "raw" messy CSV export
# ---------------------------------------------------------------------
def load_raw_data(n=150, seed=7):
    rng = np.random.default_rng(seed)
    cities = ["Hyderabad", "Chennai", "Bangalore", "Pune", "Hyderabad"]  # intentional dup-style noise
    df = pd.DataFrame({
        "student_id": np.arange(1, n + 1),
        "city": rng.choice(cities, size=n),
        "python_score": rng.uniform(40, 100, size=n).round(1),
        "maths_score": rng.uniform(40, 100, size=n).round(1),
        "leetcode_solved": rng.integers(0, 40, size=n),
    })
    # Inject missing values on purpose, like a real messy dataset
    missing_idx = rng.choice(df.index, size=10, replace=False)
    df.loc[missing_idx, "python_score"] = np.nan
    # Inject duplicate rows on purpose
    df = pd.concat([df, df.iloc[:5]], ignore_index=True)
    return df


raw_df = load_raw_data()
print("STAGE 1: Raw data loaded")
print(f"  Rows: {len(raw_df)}, Missing python_score: {raw_df['python_score'].isna().sum()}, "
      f"Duplicate rows: {raw_df.duplicated().sum()}")

# ---------------------------------------------------------------------
# 2. CLEAN
# ---------------------------------------------------------------------
clean_df = raw_df.drop_duplicates().copy()
clean_df["python_score"] = clean_df["python_score"].fillna(clean_df["python_score"].mean())
clean_df["city"] = clean_df["city"].astype("category")

print("\nSTAGE 2: Data cleaned")
print(f"  Rows after dedup: {len(clean_df)}, Missing values remaining: {clean_df.isna().sum().sum()}")

# ---------------------------------------------------------------------
# 3. ANALYSE
# ---------------------------------------------------------------------
city_summary = clean_df.groupby("city", observed=True).agg(
    avg_python=("python_score", "mean"),
    avg_maths=("maths_score", "mean"),
    avg_leetcode=("leetcode_solved", "mean"),
    students=("student_id", "count"),
).round(1).sort_values("avg_python", ascending=False)

correlation = clean_df["python_score"].corr(clean_df["leetcode_solved"])

print("\nSTAGE 3: Analysis")
print(city_summary)
print(f"\n  Correlation between python_score and leetcode_solved: {correlation:.2f}")

top_city = city_summary.index[0]
weakest_city = city_summary.index[-1]

# ---------------------------------------------------------------------
# 4. VISUALISE
# ---------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(11, 4))

city_summary["avg_python"].plot(kind="bar", ax=axes[0], color="teal")
axes[0].set_title("Average Python Score by City")
axes[0].set_ylabel("Avg Python Score")
axes[0].tick_params(axis="x", rotation=0)

axes[1].scatter(clean_df["python_score"], clean_df["leetcode_solved"], alpha=0.5, color="darkorange")
axes[1].set_title("Python Score vs LeetCode Solved")
axes[1].set_xlabel("Python Score")
axes[1].set_ylabel("LeetCode Problems Solved")

plt.tight_layout()
plt.savefig("pipeline_summary_charts.png", dpi=120)
plt.close()

print("\nSTAGE 4: Charts saved to 'pipeline_summary_charts.png'")

# ---------------------------------------------------------------------
# 5. REPORT
# ---------------------------------------------------------------------
print("\nSTAGE 5: Written summary")
print(f"""
  - After removing duplicate rows and filling {raw_df['python_score'].isna().sum()}
    missing python_score values with the column mean, the cleaned dataset
    has {len(clean_df)} student records across {clean_df['city'].nunique()} cities.
  - '{top_city}' has the highest average python_score
    ({city_summary.loc[top_city, 'avg_python']}), while '{weakest_city}' has the
    lowest ({city_summary.loc[weakest_city, 'avg_python']}).
  - Python score and LeetCode problems solved show a correlation of
    {correlation:.2f}, meaning {'a noticeable positive relationship' if correlation > 0.3 else 'little to no linear relationship'}
    between the two in this dataset.
""")