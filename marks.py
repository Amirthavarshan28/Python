a=int(input("enter the aptidude mark:"))
b=int(input("enter the GD mark:"))
c=(input("enter the techinal mark:"))
d=int(input("enter the HR mark:"))
total=a+b+c+d
if a>=85 and total>390 and total<=400:
    print("your eligible for job salary=30000")
elif b>=90 and total>380 and total<=390:
    print("your eligible for job salary=28000")
elif c>=80 and total>370 and total<=380:
    print("your eligible for job salary=25000")
elif d>=95 and total>=35 and total<=370:
    print("your eligible for job salary=20000")
else:
    print("not eligibile")




