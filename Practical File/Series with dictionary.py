import pandas as pd

a={"Aman":1000, "Raman":2000, "Kamal":3000}
x=pd.Series(a)
print(x)

print(x.index)
print(x.values)