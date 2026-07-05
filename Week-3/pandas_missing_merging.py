"""
Week 3 - Wednesday
Topic: Pandas - handling missing data, merging dataframes

Covers:
- Detecting missing values (isna, sum)
- Filling missing values (fillna: constant, mean, forward-fill)
- Dropping missing values (dropna)
- Merging dataframes: inner, left, right, outer joins
- Concatenating dataframes
"""

import pandas as pd
import numpy as np

# ---------------------------------------------------------------------
# 1. A DataFrame with missing values
# ---------------------------------------------------------------------
scores = pd.DataFrame({
    "student": ["Manoj", "Arjun", "Divya", "Sneha", "Karthik"],
    "python":  [85, np.nan, 90, 65, np.nan],
    "maths":   [92, 68, np.nan, 74, 81],
})
print("DataFrame with missing values:")
print(scores)

print("\nMissing value count per column:")
print(scores.isna().sum())

# ---------------------------------------------------------------------
# 2. Filling missing values
# ---------------------------------------------------------------------
filled_zero = scores.fillna(0)
print("\nFilled with 0:")
print(filled_zero)

filled_mean = scores.fillna({
    "python": scores["python"].mean(),
    "maths": scores["maths"].mean(),
})
print("\nFilled with column mean:")
print(filled_mean.round(1))

filled_ffill = scores.ffill()
print("\nForward-filled (each NaN takes the previous row's value):")
print(filled_ffill)

# ---------------------------------------------------------------------
# 3. Dropping missing values
# ---------------------------------------------------------------------
dropped = scores.dropna()
print("\nRows with ANY missing value dropped:")
print(dropped)

# ---------------------------------------------------------------------
# 4. Merging DataFrames
# ---------------------------------------------------------------------
students = pd.DataFrame({
    "student_id": [1, 2, 3, 4],
    "student":    ["Manoj", "Arjun", "Divya", "Sneha"],
    "city":       ["Hyderabad", "Chennai", "Bangalore", "Hyderabad"],
})

applications = pd.DataFrame({
    "student_id": [1, 1, 2, 3, 5],
    "university": ["Koblenz", "Chemnitz", "Chemnitz", "Hildesheim", "Hildesheim"],
    "status":     ["Submitted", "Submitted", "Submitted", "Submitted", "Submitted"],
})

print("\nStudents table:")
print(students)
print("\nApplications table:")
print(applications)

inner = pd.merge(students, applications, on="student_id", how="inner")
print("\nINNER JOIN (only students who have a matching application):")
print(inner)

left = pd.merge(students, applications, on="student_id", how="left")
print("\nLEFT JOIN (all students, application info if it exists):")
print(left)

right = pd.merge(students, applications, on="student_id", how="right")
print("\nRIGHT JOIN (all applications, student info if it exists):")
print(right)

outer = pd.merge(students, applications, on="student_id", how="outer")
print("\nOUTER JOIN (everything from both tables):")
print(outer)

# ---------------------------------------------------------------------
# 5. Concatenating DataFrames (stacking rows)
# ---------------------------------------------------------------------
new_students = pd.DataFrame({
    "student_id": [6, 7],
    "student":    ["Meena", "Rahul"],
    "city":       ["Chennai", "Bangalore"],
})
all_students = pd.concat([students, new_students], ignore_index=True)
print("\nConcatenated student list (original + new):")
print(all_students)