print("Welcome to my quiz game")

startGame = input("Do you want to play? ")

if startGame.lower() != "yes":
    quit()

print("Lets play then")
score = 0

answer = input("What are Pythn Data Types? ")
if answer.lower()  == "string,number,list,tuple,dictionary":
    print("Correct")
    score += 1
else:
    print("wrong")

answer = input("Is Python case-sensitive? ")
if answer.lower()  == "Yes":
    print("Correct")
    score += 1
else:
    print("wrong")

answer = input("How will you capitalize the first letter of a string? ")
if answer.lower()  == "capitalize()":
    print("Correct")
    score += 1
else:
    print("wrong")

answer = input("How to add values to a python array? ")
if answer.lower()  == "append()" or answer.lower()  == "extend()" or answer.lower()  == "insert()":
    print("Correct")
    score += 1
else:
    print("wrong")

answer = input("How to remove values to a python array? ")
if answer.lower()  == "pop()" or answer.lower()  == "remove()":
    print("Correct")
    score += 1
else:
    print("wrong")

print("You got " + str(score) + " correct" + " and " + str((score/5)*100) + " %" + " in total")
 