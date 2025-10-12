sum=0
a=int(input("enter the matrix number:"))
b=int(input("enter the matrix number:"))
c=int(input("enter the matrix number:"))
d=int(input("enter the matrix number:"))
for i in range(2):
    for j in range(2):
        if i==0 and j==0:
            sum+=a
        elif i==0 and j==1:
            sum+=b
        elif i==1 and j==0:
            sum+=c
        elif i==1 and j==1:
            sum+=d
            


print(sum)



