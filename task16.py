import pandas as pd

data = {
    "Math": [80,90],
    "Science":[70,95]
}

df = pd.DataFrame(data)

df["Total"] = df["Math"] + df["Science"]

print(df)