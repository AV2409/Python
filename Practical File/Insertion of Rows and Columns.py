import pandas as pd

df=pd.DataFrame({"Roll_no":[1,2,3,4,5],"Name":["Aman","Ram","Raman","Tarun","Sham"],"Class":[10,10,10,10,10]})
print(df)
print()
df.loc[5]=[6,"Param",10]
print(df)
"""print()
df["Fee"]=[10000,10000,11000,14000,10000] #Method--1
print(df)
print()
df.loc[:,"Fee"]=[10000,10000,11000,14000,10000] #Method--2
print(df)
print()
df=df.assign(Fee=[10000,10000,11000,14000,10000]) #Method--3
print(df)
print()
df.insert(loc=3,column="Fee", value=[10000,10000,11000,14000,10000]) #Method--4
print(df)"""