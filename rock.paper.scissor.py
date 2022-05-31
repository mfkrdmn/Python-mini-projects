import random

from requests import options

userwins = 0
computerwins = 0

options = ["rock", "paper",  "scissors"]


while True:
    userinput = input("type rock/paper/scissor or q to quit: ").lower()
    if userinput == "q":
        break

    if userinput not in options:
        continue

    randomnumber = random.randint(0,2) #rock: 0, paper: 1, scissorts: 2

    computerpick = options[randomnumber]

    print("computer picked", computerpick + ".")

    if userinput == "rock" and computerpick == "scissors":
        print("You won")
        userwins += 1
     
    
    elif userinput == "paper" and computerpick == "rock":
        print("You won")
        userwins += 1
        
         
    elif userinput == "scissors" and computerpick == "paper":
        print("You won")
        userwins += 1
       
    else:
        print("you lost")
        computerwins += 1
    
print("you won", userwins, "times")
print("computer wins" , computerwins, "times")
print("Goodbye")