import matplotlib.pyplot as plt

labels = ['India', 'US', 'Canada', 'Switzerland', 'Dubrovnik']
data = [67, 45, 34, 23, 42]
plt.scatter(labels, data, marker='s', s=50, color='grey')
plt.minorticks_on()
plt.show()
