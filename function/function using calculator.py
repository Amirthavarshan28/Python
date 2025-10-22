def calucaltor(a,b,c):
    if c=="add":
        print("addition:",a+b)
    elif c=="sub":
        print("subraction:",a-b)
    elif c=="mul":
        print("multiplication:",a*b)
    elif c=="div":
        print("division:",a/b)
d=int(input("enter the first number:"))
e=int(input("enter the second number:"))
f=input("enter the operation like add/sub/div/mul:")
calucaltor(d,e,f)
      
