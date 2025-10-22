a={'a','m','i','r','t','h','a','v','a','r','s','h','a','n','o'}
count=0
for i in a:
    if i in 'aeiou':
        count+=1
        print('vowels in set;',i)
print("number of times:",count)
