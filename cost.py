price=100
q=int(input("enter the quantity value:"))
c = price*q
if c>1000:
    d=c*0.1
    total=c-d
    print("discount offered ",total)
    
else:
    print("no discount")
