import pandas as pd

df=pd.DataFrame({"Roll_no":[1,2,3],"Name":["Ram","Tarun","Sham"],"Class":[10,10,10]})
df=df.set_index(["Name"])
print(df)
print()
df=df.reset_index()
print(df)
