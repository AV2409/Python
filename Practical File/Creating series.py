import pandas as pd

a=[10,20,30,44,56,68]
x=pd.Series(a)
x.name="My series"
print(x)

y=pd.Series([10,30,67,88,90], index=['a','b','c','d','e'])
print(y)

