
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# -----------------------------------
# 1. CREATE DATASET
# -----------------------------------

df = pd.DataFrame({
    "Name": [
        "A", "B", "C", "D",
        "E", "F", "G", "H"
    ],
    "Sex": [
        "male", "female", "female", "male",
        "female", "male", "female", "male"
    ],
    "Pclass": [3, 1, 2, 1, 3, 2, 1, 3],
    "Age": [22, 38, 26, 35, 18, 40, 30, 50],
    "SibSp": [1, 1, 0, 1, 0, 0, 1, 0],
    "Parch": [0, 0, 0, 0, 1, 0, 0, 0],
    "Fare": [7.25, 71.28, 7.92, 53.10, 8.05, 13.00, 80.00, 10.00],
    "Survived": [0, 1, 1, 0, 1, 0, 1, 0]
})

print("DATASET")
print(df)


# -----------------------------------
# 2. SURVIVAL RATE BY SEX
# -----------------------------------

sex_rate = df.groupby("Sex")["Survived"].mean()

print("\nSURVIVAL RATE BY SEX")
print(sex_rate)


# -----------------------------------
# 3. BAR CHART
# -----------------------------------

plt.figure(figsize=(6, 4))

plt.bar(
    sex_rate.index,
    sex_rate.values
)

plt.xlabel("Sex")
plt.ylabel("Survival Rate")
plt.title("Survival Rate by Sex")

plt.show()


# -----------------------------------
# 4. AGE DISTRIBUTION - HISTOGRAM
# -----------------------------------

plt.figure(figsize=(6, 4))

plt.hist(
    df["Age"],
    bins=5,
    edgecolor="black"
)

plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age Distribution")

plt.show()


# -----------------------------------
# 5. CREATE AGE GROUPS USING pd.cut()
# -----------------------------------

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=[0, 18, 30, 50, 100],
    labels=["Child", "Young", "Adult", "Senior"]
)

age_rate = df.groupby(
    "AgeGroup",
    observed=True
)["Survived"].mean()

print("\nSURVIVAL RATE BY AGE GROUP")
print(age_rate)


# -----------------------------------
# 6. CREATE FAMILY SIZE
# -----------------------------------

df["FamilySize"] = (
    df["SibSp"] +
    df["Parch"] +
    1
)

family_rate = df.groupby(
    "FamilySize"
)["Survived"].mean()

print("\nSURVIVAL RATE BY FAMILY SIZE")
print(family_rate)


# -----------------------------------
# 7. PIVOT TABLE
# -----------------------------------

pivot = df.pivot_table(
    values="Survived",
    index="Sex",
    columns="Pclass",
    aggfunc="mean"
)

print("\nPIVOT TABLE")
print(pivot)


# -----------------------------------
# 8. HEATMAP
# -----------------------------------

plt.figure(figsize=(6, 4))

sns.heatmap(
    pivot,
    annot=True,
    fmt=".1%",
    cmap="RdYlGn",
    vmin=0,
    vmax=1
)

plt.title("Survival Rate by Sex and Class")

plt.show()


# -----------------------------------
# 9. CORRELATION MATRIX
# -----------------------------------

numeric_df = df.select_dtypes(
    include="number"
)

corr = numeric_df.corr()

print("\nCORRELATION MATRIX")
print(corr.round(2))


# -----------------------------------
# 10. CORRELATION HEATMAP
# -----------------------------------

plt.figure(figsize=(8, 6))

sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    center=0
)

plt.title("Correlation Heatmap")

plt.show()


# -----------------------------------
# 11. SUMMARY OF FINDINGS
# -----------------------------------

overall_rate = df["Survived"].mean()

print("\n" + "=" * 55)
print("SUMMARY OF FINDINGS")
print("=" * 55)


# Overall survival rate

print(
    f"\n1. Overall Survival Rate: "
    f"{overall_rate:.1%}"
)


# Survival by Sex

print("\n2. Survival by Sex:")

for sex, rate in sex_rate.items():
    print(f"   {sex}: {rate:.1%}")

best_sex = sex_rate.idxmax()
worst_sex = sex_rate.idxmin()

print(
    f"   Finding: {best_sex.capitalize()} passengers had "
    f"a higher survival rate than {worst_sex} passengers."
)


# Survival by Class

class_rate = df.groupby(
    "Pclass"
)["Survived"].mean()

print("\n3. Survival by Passenger Class:")

for pclass, rate in class_rate.items():
    print(f"   Class {pclass}: {rate:.1%}")

best_class = class_rate.idxmax()
worst_class = class_rate.idxmin()

print(
    f"   Finding: Class {best_class} had the highest survival "
    f"rate, while Class {worst_class} had the lowest."
)


# Survival by Age Group

print("\n4. Survival by Age Group:")

for group, rate in age_rate.items():
    print(f"   {group}: {rate:.1%}")

best_age = age_rate.idxmax()

print(
    f"   Finding: {best_age} had the highest survival rate "
    f"in this dataset."
)


# Family Size

print("\n5. Survival by Family Size:")

for size, rate in family_rate.items():
    print(
        f"   Family Size {size}: {rate:.1%}"
    )

best_family = family_rate.idxmax()

print(
    f"   Finding: Family size {best_family} had the "
    f"highest survival rate."
)


# Sex and Class

print("\n6. Sex and Passenger Class:")

print(pivot.round(2))

print(
    "\n   Finding: The heatmap shows how survival changes "
    "when Sex and Passenger Class are analyzed together."
)


# Correlation

print("\n7. Correlation with Survival:")

corr_survived = corr["Survived"].sort_values(
    ascending=False
)

print(corr_survived.round(2))

print(
    "\n   Finding: Positive correlation values show a "
    "positive relationship, while negative values show "
    "a negative relationship."
)


print("\n" + "=" * 55)
print("VISUALIZATION ANALYSIS COMPLETED")
print("=" * 55)