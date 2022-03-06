import pandas as pd

df = pd.read_csv("final.csv")

del df["luminosity"]

df.to_csv('main.csv') 