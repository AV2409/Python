import pandas as pd

"""x=pd.Series([1,2,3,4,5],index=['a','b','c','d','e'])
x.name="My Series"
print(x)"""

x=pd.Series([12,13,45,76,45,35])
print(x)
print()
print(x[0])
print()
print(x[1:4])
print()
print(x[-5:-1])
print(x[::-1])
print(x[1::2])

"""a={"Aman":1000, "Raman":2000, "Kamal":3000}
x=pd.Series(a)
print(x)

print(x.index)
print(x.values)"""

"""x=pd.Series([10,20,30,40,50])
print(x)
print()
print(x+2)
print()
print(x-5)
print()
print(x*2)
print()
print(x/10)
print()
print(x**2)
print()
print(x==50)
print()
print(x>20)
print()
print(x[x<=30])
print()
x1=pd.Series(7, index=[1,2,3,4])
print(x1)"""

"""x=pd.Series([10,30,67,88,90,60,99,101,187])
print(x.head()) #Used to view first 5 values
print(x.tail()) #Used to view bottom 5 values
print(x.head(6)) #Used to view first 6 values
print(x.tail(7)) #Used to view bottom 7 values"""

"""a=["Aman", "Raman", "Kamal"]
b=[10,10,10]
c=[1,2,3]
d={"Name": a, "Class": b, "Roll_no": c}
df1=pd.DataFrame(d,columns=["Roll_no","Name","Class"])
print(df1)
print()
df2=pd.DataFrame({"Roll_no": [1, 2, 3],"Name": ["Ram", "Tarun", "Sham"],"Class": [10, 10, 10]})
print(df2)
print(df1["Name"])"""

"""df=pd.DataFrame({"Roll_no":[1,2,3],"Name":["Ram","Tarun","Sham"],"Class":[10,10,10]}, index=['a','b','c'])
print(df)
print()
print(df.iloc[:,[0,1]])
print()
print(df.loc[0:2])      #2 index is included
print()
print(df.iloc[0:2])     #2 index not included
print()
print(df.iloc[:,0:1])

print(df.loc['a':'b'])
#print(df.iloc['a':'b']) #Doesnot work"""

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
print(df)
print()
df["Fee"]=[10000,10000,11000,14000,10000] #Method--1
print(df)
print()
df.loc[:,"Fee"]=[10000,10000,11000,14000,10000] #Method--2
print(df)
print()
df=df.assign(Fee=[10000,10000,11000,14000,10000]) #Method--3
print(df)
print()
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
df1=df.rename(columns={"Name":"Stu_Name","Class":"Division"},index={0:"Zero",1:"One",2:"Two",3:"Three",4:'Four'},inplace=True)
print()
print(df)"""

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

"""df = pd.DataFrame({'X':[1,2,3],'Y':[100,200,300],'C':[1000,2000,3000]})
print(df)
print(df['C'].sum())
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
print(df.size)
print(df.info)"""

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