import numpy as np
import pandas as pd
from pathlib import Path

fname = Path(__file__).resolve().parent.parent / "datasets" / "cartwheeldata.csv"
df = pd.read_csv(fname)
print(type(df))

print(df.head())

print(df.columns)

print(df.iloc[1:3, 1])

# print(df.dtypes)

if (df.Gender == df["Gender"]).all():
    print(True)

print(df.Gender.unique())

print(df.loc[:, ["Gender", "GenderGroup"]])

print("Group gender and gender group")
print(df.groupby(["Gender", "GenderGroup"]).size())