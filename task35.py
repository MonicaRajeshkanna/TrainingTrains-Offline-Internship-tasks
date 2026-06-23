import pandas as pd

dates = pd.date_range("2025-01-01", periods=5)

series = pd.Series([10,20,15,18,22], index=dates)

print(series)