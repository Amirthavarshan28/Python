temp=int(input("enter the temperature:"))
if temp<0:
    print("freezing weather")
elif temp>0 and temp<10:
    print(" very cold weather")
elif temp>=10 and temp<20:
    print("cold weather")
elif temp>=20 and temp<30:
    print("normal")
elif temp>=30and temp<40:
    print("its hot")
elif temp>=40:
    print("its very hot")
else:
    print("wrong temperature")
    
