sal=int(input("enter the number:"))
age=int(input("enter the age:"))
if (sal>=  20000 or age <= 25):
    loan=int(input(" enter the loan amount:"))
    if (loan <=50000):
        print("you are eligible")
    else:
            print(" you are not loan because maximum amount loan is50000 only")
else:
                print("you are not elgible")
