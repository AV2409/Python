a=[10,20,30,40,50,60,70,80,90]
print(a)
number=int(input("Enter your number"))
pos=0
k=0
for i in a:
    if number==i:
        print(f"{number} is found and psition {pos}")
        k=1
        break
    pos=pos+1
if k==0:
    print(f"{number} does not exist")
