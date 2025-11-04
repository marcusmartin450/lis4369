#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import datetime as dt

# Try to import pandas_datareader (install with: pip install pandas-datareader)
try:
    import pandas_datareader.data as pdr
except ImportError as e:
    raise SystemExit(
        "pandas-datareader is required. Install it with:\n"
        "  pip install pandas-datareader"
    ) from e

# ----- Date range -----
start = dt.datetime(2016, 1, 1)
end = dt.datetime(2024, 10, 15)
# end = dt.datetime.now()  # uncomment to always pull through 'today'

# ----- Read data from FRED into a DataFrame -----
# Example for a single series:
# df = pdr.DataReader("GDP", "fred", start, end)

# Multiple series (Dow Jones & S&P 500):
df = pdr.DataReader(["DJIA", "SP500"], "fred", start, end)

print("\nPrint number of records:")
print(df.shape[0])

print("\nColumn names:")
print(df.columns)

print("\nPrint data frame (truncated by pandas display rules):")
print(df)

print("\nPrint first five lines:")
print(df.head())

print("\nPrint last five lines:")
print(df.tail())

print("\nPrint first 2 lines:")
print(df.head(2))

print("\nPrint last 2 lines:")
print(df.tail(2))

# ----- Plotting -----
style.use("ggplot")
ax = df["DJIA"].plot(figsize=(10, 5), label="DJIA")
df["SP500"].plot(ax=ax, label="SP500")
plt.legend()
plt.title("DJIA vs S&P 500 (FRED)")
plt.xlabel("Date")
plt.ylabel("Index Level")
plt.tight_layout()
plt.show()
