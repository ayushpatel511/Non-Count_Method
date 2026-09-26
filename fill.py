import pandas as pd
import numpy as np
df=pd.read_csv("pretics.csv")
df["City"] = df["City"].fillna("Unknown")
print(df)