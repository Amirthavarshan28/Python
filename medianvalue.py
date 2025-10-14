a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
c=int(input("enter the third number:"))
if b>a>c or c>a>b:
    print("median value:",a)
elif a>b>c or c>b>a:
    print("median value:",b)
elif b>c>a or a>c>b:
    print("median value:",c)
else:
    print("invalid")
