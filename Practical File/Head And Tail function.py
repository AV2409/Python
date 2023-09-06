import pandas as pd

x=pd.Series([10,30,67,88,90,60,99,101,187])
print(x.head()) #Used to view first 5 values
print(x.tail()) #Used to view bottom 5 values
print(x.head(6)) #Used to view first 6 values
print(x.tail(7)) #Used to view bottom 7 values
