import pandas as pd

# Sample messy dataset
df = pd.DataFrame({
    "Name": [" Manoj ", "Ravi", "Sita ", "Anil", " Kiran"],
    "Age": ["22", "25", "unknown", "30", "200"],
    "Salary": [30000, 40000, None, 50000, 45000],
    "City": ["HYDERABAD", "hyderabad", " Hyderabad ", "VIZAG", "vizag"]
})

print("ORIGINAL DATA")
print(df)

# -----------------------------------
# 1. CHECK MISSING VALUES
# -----------------------------------
print("\nMISSING VALUES")
print(df.isnull().sum())

# Fill missing Salary with mean
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# -----------------------------------
# 2. CHANGE DATA TYPE
# -----------------------------------
# Convert Age to numeric
# Invalid value "unknown" becomes NaN
df["Age"] = pd.to_numeric(df["Age"], errors="coerce")

# Fill missing Age with mean
df["Age"] = df["Age"].fillna(df["Age"].mean())

print("\nAFTER FIXING DATA TYPES")
print(df)
print("\nDATA TYPES")
print(df.dtypes)

# -----------------------------------
# 3. FORMAT TEXT DATA
# -----------------------------------
# Remove extra spaces
df["Name"] = df["Name"].str.strip()
df["City"] = df["City"].str.strip()

# Make City formatting consistent
df["City"] = df["City"].str.title()

print("\nAFTER TEXT FORMATTING")
print(df)

# -----------------------------------
# 4. DETECT OUTLIERS USING IQR
# -----------------------------------
Q1 = df["Age"].quantile(0.25)
Q3 = df["Age"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

print("\nOUTLIER LIMITS")
print("Lower limit:", lower_limit)
print("Upper limit:", upper_limit)

# Find outliers
outliers = df[
    (df["Age"] < lower_limit) |
    (df["Age"] > upper_limit)
]

print("\nOUTLIERS")
print(outliers)

# -----------------------------------
# FINAL CLEANED DATA
# -----------------------------------
print("\nFINAL CLEANED DATA")
print(df)