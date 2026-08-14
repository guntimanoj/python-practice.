import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------------
# SAMPLE DATA
# -----------------------------------
df = pd.DataFrame({
    "Age": [20, 22, 25, 30, 35, 40, 45, 50],
    "Experience": [1, 2, 3, 5, 7, 10, 12, 15],
    "Salary": [20000, 25000, 30000, 40000, 50000, 60000, 70000, 85000]
})

print("DATA")
print(df)

# -----------------------------------
# 1. MEAN
# -----------------------------------
print("\nMEAN")
print(df.mean(numeric_only=True))

# -----------------------------------
# 2. STANDARD DEVIATION
# -----------------------------------
print("\nSTANDARD DEVIATION")
print(df.std(numeric_only=True))

# -----------------------------------
# 3. CORRELATION
# -----------------------------------
print("\nCORRELATION MATRIX")
print(df.corr(numeric_only=True))

# Correlation between Experience and Salary
correlation = df["Experience"].corr(df["Salary"])

print("\nEXPERIENCE vs SALARY CORRELATION")
print(correlation)

# -----------------------------------
# 4. DISTRIBUTION
# -----------------------------------
print("\nSTATISTICAL SUMMARY")
print(df.describe())

print("\nAGE FREQUENCY DISTRIBUTION")
print(df["Age"].value_counts().sort_index())

# -----------------------------------
# 5. HISTOGRAM
# -----------------------------------
plt.hist(df["Age"], bins=5)
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution")
plt.show()