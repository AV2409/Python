import pandas as pd

df= pd.DataFrame({'ID':[10101,10102,10103],'Name':['karan','rupan bal','Stalin'],'salary':[100000,200000,300000]})
print(df)
df.to_csv('E:\Practical file\employee.csv')
