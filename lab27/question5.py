import pandas as pd
import numpy as np

# Read CSV file
df = pd.read_csv("diabetes.csv")

# (i) Print all column names
print("Column Names:")
print(df.columns)

# (ii) Print first 10 rows
print("\nFirst 10 Rows:")
print(df.head(10))

# (iii) Mean of BloodPressure
print("\nMean Blood Pressure:")
print(df["BloodPressure"].mean())

# (iv) First 4 rows of columns 3, 4, 5
print("\nFirst 4 Rows of Columns 3, 4, 5:")
print(df.iloc[:4, 2:5])

# (v) Normalization
BP = df["BloodPressure"]

df["NormalizedBP"] = (
    (BP - BP.min()) / (BP.max() - BP.min())
)

print("\nNormalized Blood Pressure:")
print(df[["BloodPressure", "NormalizedBP"]].head())

# (vi) Categorize Age

def categorize_age(age):

    if age >= 1 and age <= 18:
        return "Youth"

    elif age >= 19 and age <= 50:
        return "Adult"

    else:
        return "Senior"


df["age category"] = df["Age"].apply(categorize_age)

print("\nAge Categories:")
print(df[["Age", "age category"]].head())