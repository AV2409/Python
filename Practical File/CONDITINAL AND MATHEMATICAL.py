import pandas as pd

df = pd.DataFrame({'x':[17,2,53],'y':[456,35,6],'z':[7,28,9]})
print(df)
df1 = pd.DataFrame({'x':[181,2,73],'y':[4,65,64],'z':[7,38,97]})
print(df1)
print(df.eq(df1))
print(df.gt(df1))
print(df.lt(df1))
print(df.add(df1))
print(df.sub(df1))
print(df.mul(df1))
print(df.rdiv(df1))
print(df.rsub(df1))
print(df.div(df1))
