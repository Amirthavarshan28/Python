a={1,2,3,4,5,6,7,8,9,10}
b=[]
c=[]
for i in a:
   if i%2==1:
             b.append(i)
             
   else:
       c.append(i)
       
print("even number is:",set(c))
       
print("odd number is :",set(b))

