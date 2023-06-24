num = int(input("Enter number (1-7): "))
week = ["", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
if 0 < num < 8:
    print(week[num])
else:  
    print("Your number should be between 1 and 7.")


