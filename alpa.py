a=input("enter the string:")
b="abcdefghijklmnopqurstuvwxyzABCDEFGHIJKLMNOPQURSTUVWXYZ"
for i in a:
    if i in b:
        print( "only alphabets")
    else:
        print("not alphabets and characters")
