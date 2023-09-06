import pandas as pd

df=pd.DataFrame({"Roll_no":[1,2,3],"Name":["Ram","Tarun","Sham"],"Class":[10,10,10]})
print(df)
print()
print(df.iloc[:,[0,1]])
print()
print(df.loc[0:2])      #2 index is included
print()
print(df.iloc[0:2])     #2 index not included
print()
print(df.iloc[:,0:1])

#print(df.loc['a':'b'])
#print(df.iloc['a':'b']) #Doesnot work

