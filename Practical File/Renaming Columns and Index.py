import pandas as pd

df=pd.DataFrame({"Roll_no":[1,2,3,4,5],"Name":["Aman","Ram","Raman","Tarun","Sham"],"Class":[10,10,10,10,10]})
print(df)
df.rename(columns={"Name":"Stu_Name","Class":"Division"},index={0:"Zero",1:"One",2:"Two",3:"Three",4:'Four'},inplace=True)
print()
print(df)
