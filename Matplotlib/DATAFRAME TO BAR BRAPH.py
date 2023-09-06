import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame({'name':['justin','Jamie','Tywin','Tyrion'],'maths':[64,47,35,34],'English':[34,46,34,87]})
df.plot(kind='bar',figsize=(9,9),ylim=(0,100),x='name')
plt.ylabel('marks')
plt.show()
