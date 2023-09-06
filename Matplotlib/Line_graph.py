import matplotlib.pyplot as plt
plt.figure('My Chart') #To change name of window
x=['Maths','Science','IP','SST']
a =int(input("Enter the marks of 1st subject"))
stu_1=[a,98,100,95]
stu_2=[80,74,75,68]
stu_3=[78,62,98,95]
plt.plot(x,stu_1,color='aqua',marker='d',lw=2,ls='-.')
plt.plot(x,stu_2,color='lawngreen',marker='o',lw=2)
plt.plot(x,stu_3,color='red',marker='s',lw=2)
plt.legend(['stu_1','stu_2','stu_3'],loc='lower right',fontsize=13)
plt.title('Student Performance',fontweight='bold', fontsize=23)
plt.xlabel('Subject',fontweight='bold', fontsize=15)
plt.ylabel('Marks',fontweight='bold', fontsize=15)
plt.grid(which='major',color='black',lw=1.5)
plt.grid(which='minor',color='lightgrey',ls="-")
plt.minorticks_on()
plt.xlim(-1,4)
plt.ylim(0,100)
#plt.gcf().canvas.set_window_title('My Chart')

plt.show()
