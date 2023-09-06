while (True):
    print("1. - Area of Circle ")
    print("2. - Area of Square ")
    print("3. - Area of Rectangle ")
    print("4. - Quit")
    print()
    x = int(input("Choose your option "))
    if x==1:
        r = int(input("Enter the radius"))
        pi=3.14
        area = (3.14)*r*r
        print(f"Area of circle is {area}")
    if x==2:
        s = int(input("Enter the side of square"))
        area =  s*s
        print(f"Area of square is {area}")
    if x==3:
        l = int(input("Enter the lenght of rectangle"))
        b = int(input("Enter the breadth of rectangle"))
        area =  l*b
        print(f"Area of Rectangle is {area}")
    if x==4:
        print("Exit Successful")
        break
    print()


