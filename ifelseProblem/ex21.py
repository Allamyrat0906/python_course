x=int(input("x enter "))
y=int(input("y enter "))

if x==0 and y==0:
    print(0)
elif y==0 and x>0:
    print(1)
elif x==0 and y>0:
    print(2)
else:
    print(3)