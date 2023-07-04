count_e=int(input("How many employees to join: "))
employers=[]

for i in range(count_e):
    addemployer=input("Add employee: ").lower()
    if addemployer!= int or " " or None or float: 
    #if addemployer== str: 
        continue
    else:
        print("not adding employee")
    addemployer=addemployer.capitalize()
    employers.append(addemployer)
    employers.sort()
    print(employers)
else:
    print("No more employees to join")