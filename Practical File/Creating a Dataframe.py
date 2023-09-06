import pandas as pd

a=["Aman", "Raman", "Kamal"]
b=[10,10,10]
c=[1,2,3]
d={"Name": a, "Class": b, "Roll_no": c}
df1=pd.DataFrame(d,columns=["Roll_no","Name","Class"])
print(df1)
print()
df2=pd.DataFrame({"Roll_no": [1, 2, 3],"Name": ["Ram", "Tarun", "Sham"],"Class": [10, 10, 10]})
print(df2)
print(df1["Name"])
