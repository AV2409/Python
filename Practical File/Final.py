import pandas as pd
"""d=["Virat",'Rohit',"Warner"]
e=[10,40,22,25,26,30,35]
s2=pd.Series(e)
s1=pd.Series(d)
s3=pd.Series(dtype=float)
print(s1)
print()
print(s1.index)
print()
print(s1.values)
print()
print(s1[s2<30])
print()
print(s2.shape)
print()
print(s3.empty)"""

"""df1=pd.DataFrame({"Name":['Karan','Charan','Raman'],"Class":[10,10,10],"Rollno":[1,2,3]},index=['a','b','c'], columns=['Rollno','Class','Name'])
print(df1)
print()
print(df1.loc['a':'b'])
print()
print(df1.iloc[[0,2],[0,2]])
print()
print(df1.iloc[0:2,1:3])
print()
print(df1.iloc[[0,2],1:3])"""

"""df=pd.DataFrame({"Roll_no":[1,2,3],"Name":["Ram","Tarun","Sham"],"Class":[10,10,10]})
df=df.set_index(["Name"])
print(df)
print()
df=df.reset_index()
print(df)"""

"""df=pd.DataFrame({"Roll_no":[1,2,3,4,5],"Name":["Aman","Ram","Raman","Tarun","Sham"],"Class":[10,10,10,10,10]})
print(df)
print()
df.loc[5]=[6,"Param",10]
#print(df)
print()
#df["Fee"]=[10000,10000,11000,14000,10000] #Method--1
#print(df)
print()
#df.loc[:,"Fee"]=[10000,10000,11000,14000,10000] #Method--2
#print(df)
#print()
#df=df.assign(Fee=[10000,10000,11000,14000,10000]) #Method--3
#print(df)
#print()
df.insert(loc=3,column="Fee", value=[10000,10000,11000,14000,10000,15000]) #Method--4
print(df)"""

"""df1=pd.DataFrame({"Roll_no":[1,2,3],"Name":["Aman","Ram","Raman"],"Class":[10,10,10]})
print(df1)
print()
df2=pd.DataFrame({"Roll_no":[4,5],"Name":["Tarun","Sham"],"Class":[10,10]})
#df=df1.append(df2,ignore_index=True) #Method--1
#print(df)
df=pd.concat([df1,df2],ignore_index=True) #Method--2
print(df)"""

"""df=pd.DataFrame({"Roll_no":[1,2,3,4,5],"Name":["Aman","Ram","Raman","Tarun","Sham"],"Class":[10,10,10,10,10]})
print(df)
#df1=df.rename(columns={"Name":"Stu_Name","Class":"Division"},index={0:"Zero",1:"One",2:"Two",3:"Three",4:'Four'},inplace=True)
print()
print(df1)"""

"""df1=pd.DataFrame({"Roll_no":[1,2,3,4,5],"Name":["Aman","Ram","Raman","Tarun","Sham"],"Class":[10,10,10,10,10]})
df2=pd.DataFrame({"Roll_no":[1,2,3,4,5],"Name":["Aman","Ram","Raman","Tarun","Sham"],"Class":[10,10,10,10,10]})
print(df1)
print()
print(df1.drop(0))
print()
print(df1.drop([1,2],axis=0))
print()
print(df2.drop("Class",axis=1))
print()
print(df2.drop(["Name","Class"],axis=1))"""

"""df = pd.DataFrame({'X':['a','b','c'],'Y':[100,200,300],'C':[1000,2000,3000]})
print(df)
print(df["C"].sum())
print(df.loc[:,'Y':'C'].sum())
print(df.sum())
print(df.max())
print(df.min())
print(df.mean())
print(df.median)
print(df.count())

print(df.sum(axis=1))
print(df.max(axis=1))
print(df.min(axis=1))
print(df.mean(axis=1))
print(df.median)
print(df.count(axis=1))"""

"""df = pd.read_csv("E:\Practical file\Book1.csv")

print(df)"""

"""df= pd.DataFrame({'ID':[10101,10102,10103],'Name':['karan','rupan bal','Stalin'],'salary':[100000,200000,300000]})
print(df)
df.to_csv('E:\Practical file\employee.csv')"""

"""df = pd.read_csv("E:\Practical file\Book1.csv")
print(df)
df = pd.read_csv("E:\Practical file\Book1.csv", header=None)
print(df)
df = pd.read_csv("E:\Practical file\Book1.csv", usecols=['Class', 'Name'])
print(df)"""

"""df = pd.DataFrame({'x':[1,2,3],'y':[4,5,6],'z':[7,8,9]})
print(df)

print(df.shape)
print(df.size)
print(df.info)
print(df.ndim)"""

"""df = pd.DataFrame({'x':[17,2,53],'y':[456,35,6],'z':[7,28,9]})
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
print(df.div(df1))"""

"""df1=pd.DataFrame({"Name":['Karan','Charan','Raman'],"Class":[10,10,10],"Rollno":[1,2,3]},index=['a','b','c'], columns=['Rollno','Class','Name'])
print(df1)

for (a,b) in df1.iterrows():
    #print(b)
    print(b["Name"])
    #print("Row Index:", a, '\n' "Values:",b)

for(a,b) in df1.iteritems():
    print("Column index:",a ,'\n')
    #print(b)
    for i in b:
        print(i)"""

"""print()
for(a,b) in df1.iteritems():
    print("Column index:",a ,'\n')
    print(b)"""

"""S1 = pd.Series([1, 2, 3, 4], index = ['a', 'b','c','d'])
S2 = pd.Series([11, 22, 33, 44], index = ['a', 'bb','c','dd'])
D1 = pd.DataFrame([S1,S2])
print(D1)"""

"""s1=pd.Series([1,2,3], index=['a','b','c'])
s2=pd.Series([1,2,3], index=['a','c','d'])
print(s1)
print()
print(s2)
print()
print(s1.add(s2))
print(s2.add(s1, fill_value=0))"""

s1=pd.Series(data=2*(3,10))
print(s1)