"""
Week 3 - Monday
Topic: Pandas - Series, DataFrames, reading CSV and Excel

Covers:
- Creating a Series (1D labeled array)
- Creating a DataFrame (2D labeled table) from a dict
- Writing a DataFrame to CSV and Excel
- Reading it back from CSV and Excel
- Basic inspection methods: head, info, describe, dtypes, shape
"""

import pandas as pd
import numpy as np

# ---------------------------------------------------------------------
# 1. Series - a single labeled column of data
# ---------------------------------------------------------------------
marks = pd.Series([78, 85, 92, 60, 74], index=["Math", "Physics", "CS", "German", "English"])
print("Series (subject marks):")
print(marks)
print("\nMean mark:", marks.mean())
print("Highest scoring subject:", marks.idxmax())

# ---------------------------------------------------------------------
# 2. DataFrame - built from a dictionary of equal-length lists
# ---------------------------------------------------------------------
data = {
    "student":   ["Manoj", "Arjun", "Divya", "Sneha", "Karthik"],
    "python":    [85, 72, 90, 65, 78],
    "maths":     [92, 68, 88, 74, 81],
    "leetcode":  [15, 8, 22, 5, 12],
    "city":      ["Hyderabad", "Chennai", "Bangalore", "Hyderabad", "Pune"],
}
df = pd.DataFrame(data)
print("\nDataFrame:")
print(df)

# ---------------------------------------------------------------------
# 3. Basic inspection
# ---------------------------------------------------------------------
print("\nShape:", df.shape)
print("\nColumn dtypes:\n", df.dtypes)
print("\nSummary statistics:\n", df.describe())
print("\nFirst 3 rows:\n", df.head(3))

# ---------------------------------------------------------------------
# 4. Write to CSV and Excel, then read back
# ---------------------------------------------------------------------
csv_path = "students.csv"
xlsx_path = "students.xlsx"

df.to_csv(csv_path, index=False)
df.to_excel(xlsx_path, index=False)
print(f"\nSaved DataFrame to '{csv_path}' and '{xlsx_path}'")

df_from_csv = pd.read_csv(csv_path)
df_from_excel = pd.read_excel(xlsx_path)

print("\nRe-loaded from CSV:")
print(df_from_csv)

print("\nRe-loaded from Excel:")
print(df_from_excel)

# ---------------------------------------------------------------------
# 5. Sanity check - confirm round trip preserved the data
# ---------------------------------------------------------------------
assert df.equals(df_from_csv), "CSV round trip changed the data!"
assert df.equals(df_from_excel), "Excel round trip changed the data!"
print("\nRound trip check passed: CSV and Excel data match the original DataFrame.")