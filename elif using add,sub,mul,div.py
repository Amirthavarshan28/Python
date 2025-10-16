'''codition use to add,sub,mul,div'''
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
calculation= input("add/sub/mul/div:")
if calculation=="add":
    print("addition value",a+b)
elif calculation=="sub":
    print("subraction value",a-b)
elif calculation=="mul":
    print("multipication value",a*b)
elif calculation=="div":
    print("division value",a/b)
else:
    print("Invalid error")
    

