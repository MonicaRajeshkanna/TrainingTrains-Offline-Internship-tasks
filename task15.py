import pandas as pd

df = pd.read_csv("students.csv")

print("Mean")
print(df.mean(numeric_only=True))

print("Median")
print(df.median(numeric_only=True))

print("Standard Deviation")
print(df.std(numeric_only=True))