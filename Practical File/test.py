"""import matplotlib.pyplot as pline
x=[13,16,18,33,45,10,20,30,40,50]
y=[0,20,40,60]
pline.hist(x,y)

pline.xlabel('marks')
pline.show()
pline.savefig('abc.png')"""
import numpy as np
import pandas as pd

x=pd.Series(10,index=[1,2,3,4])
print(x)