"""
Week 3 - Tuesday
Topic: Pandas - filtering, sorting, groupby, aggregation

Covers:
- Boolean filtering (single and multiple conditions)
- .sort_values() with single/multiple keys
- .groupby() with single and multiple aggregations
- .agg() for custom multi-column aggregation
"""

import pandas as pd

data = {
    "student":  ["Manoj", "Arjun", "Divya", "Sneha", "Karthik", "Meena", "Rahul"],
    "city":     ["Hyderabad", "Chennai", "Bangalore", "Hyderabad", "Pune", "Chennai", "Bangalore"],
    "python":   [85, 72, 90, 65, 78, 95, 60],
    "maths":    [92, 68, 88, 74, 81, 91, 55],
    "leetcode": [15, 8, 22, 5, 12, 25, 3],
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# ---------------------------------------------------------------------
# 1. Filtering
# ---------------------------------------------------------------------
strong_python = df[df["python"] >= 80]
print("\nStudents with python score >= 80:")
print(strong_python)

strong_both = df[(df["python"] >= 75) & (df["maths"] >= 80)]
print("\nStudents strong in BOTH python (>=75) and maths (>=80):")
print(strong_both)

not_hyderabad = df[df["city"] != "Hyderabad"]
print("\nStudents NOT from Hyderabad:")
print(not_hyderabad)

# ---------------------------------------------------------------------
# 2. Sorting
# ---------------------------------------------------------------------
by_python_desc = df.sort_values("python", ascending=False)
print("\nSorted by python score (descending):")
print(by_python_desc)

by_city_then_maths = df.sort_values(["city", "maths"], ascending=[True, False])
print("\nSorted by city (A-Z), then maths (high to low) within each city:")
print(by_city_then_maths)

# ---------------------------------------------------------------------
# 3. Groupby - single aggregation
# ---------------------------------------------------------------------
avg_python_by_city = df.groupby("city")["python"].mean()
print("\nAverage python score by city:")
print(avg_python_by_city)

# ---------------------------------------------------------------------
# 4. Groupby - multiple aggregations at once
# ---------------------------------------------------------------------
city_summary = df.groupby("city").agg(
    avg_python=("python", "mean"),
    avg_maths=("maths", "mean"),
    total_leetcode=("leetcode", "sum"),
    students=("student", "count"),
)
print("\nCity-wise summary (avg python, avg maths, total leetcode solved, student count):")
print(city_summary)

# ---------------------------------------------------------------------
# 5. Groupby with sorting on the aggregated result
# ---------------------------------------------------------------------
top_city = city_summary.sort_values("avg_python", ascending=False)
print("\nCities ranked by average python score:")
print(top_city)
print(f"\nStrongest city on average python score: {top_city.index[0]}")