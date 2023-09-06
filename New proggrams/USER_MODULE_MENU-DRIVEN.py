def add(x,y):
    z=x+y
    print(z)
def sub(x,y):
    z=x-y
    print(z)
def div(x,y):
    z=x/y
    print(z)
def mul(x,y):
    z=x*y
    print(z)
while (True):
    print("1. - Addition of 2 numbers ")
    print("2. - Subtraction of 2 numbers ")
    print("3. - Division of 2 numbers ")
    print("4. - Multiplication of 2 numbers")
    print("5. - Quit")
    print()
    a = int(input("Choose your option "))
    if a==1:
        x=int(input("Enter the First number"))
        y=int(input("Enter the Second number"))
        add(x,y)
    if a==2:
        x=int(input("Enter the First number"))
        y=int(input("Enter the Second number"))
        sub(x,y)
    if a==3:
        x=int(input("Enter the First number"))
        y=int(input("Enter the Second number"))
        div(x,y)
    if a==4:
        x=int(input("Enter the First number"))
        y=int(input("Enter the Second number"))
        mul(x,y)
    if a==5:
        print("Exit Successful")
        break
    print()
