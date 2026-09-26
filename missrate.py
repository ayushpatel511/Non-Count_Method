import pandas as pd
import numpy as np
df=pd.read_csv("pretics.csv")
print(df[df["Rating"].isnull()])