a=int(input("Enter your percentage"))
if a>=90 and a<=100:
      b="A1"
elif a>=80 and a<=89:
      b="A2"
elif a>=70 and a<=79:
      b="B1"
elif a>=60 and a<=69:
      b="C1"
elif a>=50 and a<=59:
      b="C2"
elif a>=33 and a<=49:
      b="D"
elif a>=0 and a<=32:
      b="E"
else:
    b="Not possible"
print("Your grade is",b)
