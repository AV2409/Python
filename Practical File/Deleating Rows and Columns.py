import pandas as pd

df1=pd.DataFrame({"Roll_no":[1,2,3,4,5],"Name":["Aman","Ram","Raman","Tarun","Sham"],"Class":[10,10,10,10,10]})
df2=pd.DataFrame({"Roll_no":[1,2,3,4,5],"Name":["Aman","Ram","Raman","Tarun","Sham"],"Class":[10,10,10,10,10]})
print(df1)
print()
print(df1.drop(0))
print()
print(df1.drop([1,2],axis=0))
print()
print(df2.drop("Class",axis=1))
print()
print(df2.drop(["Name","Class"],axis=1))
