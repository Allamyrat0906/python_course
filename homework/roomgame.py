import random

print("Welcome Room game!!! :/ :> :) ;< ")
gamer=input("Enter your username >>>> ")
print(f"Welcome {gamer.capitalize()}.\nDo you ready to play.")
yesno=input(">>>> ").lower()
#chekyes=(yesno.lower() or yesno.upper() or yesno.capitalize())



if yesno=="yes":
    print("Let\'s start the game! ")
else:
    print("what happened :/ game is boring for you :( ")

print("okey first Level 1. Choose  1 room inside 3 rooms below ->>")
print("""
        1. room 1
        2. room 2
        3. room 3
    """)
print("hint: (if you choose room 1,  you  write just 1)")



roomchoose=int(input("Selected room >>>>  ") )

print(f"okey yo selected{roomchoose} room")

if roomchoose==1:
    while True:
        print("""
            how to play room 1: 
            
            you enter a number and 
            the number you enter must be between 1 and 10 and 
            i give a random number if yours matches the number i gived 
            you win if it doesn't you lose
        
            """) 
        my_number=int(input("Enter a number>>>> "))
        if my_number==(random.randrange(1, 10)):
            print("Yeeeeeee   you  winnn")
            exit()
        else:
            print("owww sorry you lose. Play again")

    
if roomchoose==2:
    print("""


     room2


    """)
if roomchoose==3:
    print("""


     room3


    """)


