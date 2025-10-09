a=int(input("enter the value:"))
b=int(input("enter the value:"))
c=int(input("enter the length:"))
if a==b and a==c:
    print("it is equilateral")
elif a==b or b==c or c==a:
    print("it is isosceles")
else:
    print("it is a scalene")
