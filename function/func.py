# def my_function():
#     print("my first function")

# my_function()


# name parametr 
# def second(name):
#     print(name + "  good")

# second("Allamyrat")
# second("Meylis")
# second("Gadyr")
# second("Nikita")
# second("Akmyrat")


# def more_parametr(name,lastname):
#     print("Hi {} , {}".format(name,lastname))

# more_parametr("Allamyrat", "Annayev")


# def more_and_more(*name):
#     print("Hi " + name[0])

# more_and_more("Allamyrat","Meylis" )

# def keyword(name1,name2,name3):
#     print("Hi" + " " + name1 + " and " +  name2)

# keyword(name1="Allamyrat",name2="Meylis",name3="Gadyr")


# def func1(**name):
#     print("Hi " + name["name1"])

# func1(name1="Allamyrat")


# def country(cname="Asgabat"):
#     print("Welcome to " +  cname)

# country("Dubai")
# country("moskov")
# country()
# country("Turkey")
# fruits=["apple", "banana", "orange"]
# def my_favorites_food(food):
#     for x in food:
#         print(x)


# my_favorites_food(fruits)

# def num(x):
#     print(x*x)

# num(4)


# def returnf(x):
#     return x*x

# print(returnf(3))
# #-----------------------------------
# def returnf(x):
#     print(x*x) 

# returnf(3)


# def tri_recursion(k):
#   if(k > 0):
#     result = k + tri_recursion(k - 1)
#     print(k)
#     print(result)
#   else:
#     result=0
#   return result
   
# print("\n\nRecursion Example Results")
# tri_recursion(6)

# for i in range(5):
#     a=int(input("Number : "))
#     def PowerA3(a):
#         B=a**3
#         print(B)
#     PowerA3(a)
# #---------------------------------------------------
# def PowerA(a):
#     b=a**3
#     print(b)

# for i in range(5):
#     number = int(input("Number: "))
#     PowerA(number)

# number=int(input("Number: "))
# convertstring=str(number)

# for x in convertstring:

#     print(x)
#     def DigitCountSum(covertstring):
        

# number=int(input("Number: "))
# def DigitCountSum(number):
#     count=0
#     sum=0
#     for i in str(number):
#         count=count+1
#         sum=sum+int(i)
#     print(count)
#     print(sum)
# DigitCountSum(number)
a1=int(input("A1: "))
b1=int(input("B1: "))
c1=int(input("C1: "))
a2=int(input("A2: "))
b2=int(input("B2: "))
c2=int(input("C2: "))
sortlist1=[]
sortlist2=[]
def Sort(x,y,z):
    sortlist1.append(x)
    sortlist1.append(y)
    sortlist1.append(z)
    sortlist1.sort()
    print(sortlist1)
    sortlist2.append(x)
    sortlist2.append(y)
    sortlist2.append(z)
    sortlist2.sort()
    print(sortlist2)
Sort(a1,b1,c1)
Sort(a2,b2,c2)

