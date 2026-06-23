import pandas as pd

data = {
    "Age":[20,None,25],
    "Salary":[30000,40000,None]
}

df = pd.DataFrame(data)

print(df.fillna(df.mean()))