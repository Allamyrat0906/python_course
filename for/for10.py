# n=int(input("Number: "))
# count=0
# for i in range(1,n+1):
#     count = count + (1/i)
# print(count)
# power=0
# n=int(input("Number: "))

# for i in range(n+1):
#     even=(2*i)
#     power=power+pow(even,2)
# print(power)

# res=1
# n=int(input("Number: "))
# for i in range(1,n+1):
#     res=res*(1+i/10)
# print(res)
count=0

n=int(input("Number: "))
for i in range(1,n+1):
    count=count+(i/10+1)*(pow(-1,i+1))
    print(count)

   

