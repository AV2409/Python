import matplotlib.pyplot as plt

labels = ['India','US','Canada','Switzerland','Dubrovnik']
data = [67,45,34,23,42]
plt.pie(data,labels = labels,colors =('m','r','b','g','c','y'),startangle= 45,explode=(0.1,0,0,0.2,0),shadow = True)
plt.title('Population',color='grey')
plt.legend(labels,loc='lower left')
plt.show()

