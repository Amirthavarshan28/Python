a=int(input("enter the number:"))
odd_count=0
even_count=0
for i in range(1,a+1):
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
print("odd count is:",odd_count)
print("even count is:",even_count)
        
