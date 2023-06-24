month=["January",  "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
seosons=["Winter", "Spring","Summer", "Autumn"]
num=int(input("Number : "))

for i in range(month):
    print(i)

# if num>0 and num<13:
#     m=month[num]
#     print(m)
#     if (num==12 or num==1 or num==2):
#         print(seosons[0])
#     if (num==3 or num==4 or num==5):
#         print(seosons[1])
#     if (num==6 or num==7 or num==8):
#         print(seosons[2])
#     if (num==9 or num==10 or num==11):
#         print(seosons[3])
# else:
#     print("error")


# mesyac={1 : "Январь", 
#         2 : "Февраль", 
#         3 : "Март", 
#         4 : "Апрель",
#         5 : "Май",
#         6 : "Июнь",
#         7 : "Июль",
#         8 : "Август",
#         9 : "Сентябрь",
#         10 : "Октябрь",
#         11 : "Ноябрь", 
#         12 : "Декабрь"}
# sizon={1:"Зима", 2:"Весна", 3:"Лето", 4:"Осень"}
# x=int(input("Введите номер месяца от 1 до 12: "))
# if x in [1,2,12]:
#     print("Месяц:",mesyac[x], "\n" "Время года:", sizon[1])
# elif x in [3,4,5]:
#     print("Месяц:",mesyac[x], "\n" "Время года:", sizon[2])
# elif x in [6,7,8]:
#     print("Месяц:",mesyac[x], "\n" "Время года:", sizon[3])
# elif x in [9,10,11]:
#     print("Месяц:",mesyac[x], "\n" "Время года:", sizon[4])
# elif x<1 or x>12:
#     print("Ошибка")