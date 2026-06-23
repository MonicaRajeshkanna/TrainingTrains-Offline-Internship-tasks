import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

plt.hist(df["Marks"])

plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()