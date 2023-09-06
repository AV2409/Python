import pandas as pd

"""player1={'t20':13000, 'odi':14000,'test':12000}

player2={'t20':5000,'odi':8000,'test':12000}
totSales={"playerIst":player1,"playerIInd":player2}
df=pd.DataFrame(totSales)
print(df)"""

x=[1000,2000,3000]
y=[1900,2300,4500]
z=[2000,5000,7000]
df=pd.DataFrame({'Quarter1':x,'Quarter2':y,'Quarter3':z},index=['s1','s2','s3'])
print(df)
print(df['Quarter1']+df['Quarter2'])
print(df['Quarter3'].mean())
print()
df.loc['s4']=[1200,2000,3000]
print(df)
#df1=df.rename(index={3: "s4"})
#print(df1)

"""s1=pd.Series([1,2,3,4],index=['a','b','d','f'])
s2=pd.Series([2,5,1,3],index=['a','c','d','e'])
print(s1.add(s2,fill_value=0))"""
