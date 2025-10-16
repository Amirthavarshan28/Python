"entered the names is add after stop means stop list"
a=[]
for i in range (100):
    b=input("enter the name or stop:")
    if b == "stop":
        break
    a.append(b)
          
print("after enter stop",a)       
