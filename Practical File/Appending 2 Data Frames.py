import pandas as pd

df1=pd.DataFrame({"Roll_no":[1,2,3],"Name":["Aman","Ram","Raman"],"Class":[10,10,10]})
print(df1)
print()
df2=pd.DataFrame({"Roll_no":[4,5],"Name":["Tarun","Sham"],"Class":[10,10]})
#df=df1.append(df2,ignore_index=True) #Method--1
#print(df)
df=pd.concat((df1,df2),ignore_index=True) #Method--2
print(df)
