import pandas as pd

df = pd.read_csv("E:\Practical file\Book1.csv")
print(df)
df = pd.read_csv("E:\Practical file\Book1.csv", header=None)
print(df)
df = pd.read_csv("E:\Practical file\Book1.csv", usecols=['Class', 'Name'])
print(df)
