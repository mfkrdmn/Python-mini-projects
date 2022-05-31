import random

top = input("Type a number ")

if top.isdigit():  #The isdigit() method returns True if all the characters are digits(numeric), otherwise False.
    top = int(top)

    if top <= 0:
        print("please type a number greater than 0 next time")
        quit()
else:
    print("Please type a number next time")
    quit()

randomnumber = random.randint(0,top)


while True:
    user = input("make a guess: ")
    if user.isdigit():  
        user = int(user)
    else:
        print("Please type a number next time")
        continue

    if user == randomnumber:
        print("you got it")
        break
    elif user > randomnumber:
        print("You are above the number")
    else:
        print("you got it wrong")
