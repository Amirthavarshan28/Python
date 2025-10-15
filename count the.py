a=input("enter the string:")
b=a.split()
count=0
for i in b:
    if "the" in i:
        count+=1
print(i,"=",count)
