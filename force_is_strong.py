import random

print("Welcome to a Star Wars themed Guessing Game!")
print("The computer has picked a number 1-10, try to match it")
comp = random.randint(1,10)
user = int(input("Enter your guess: "))
print("You picked " + str(user) + " the number was " + str(comp))

if comp == user :
    msg = "Honored to play with you Master"
elif comp - user == 1 or comp - user == -1:
    msg = "You are a worthy opponent Knight"
elif comp - user == 2 or comp - user == -2:
    msg = "You have much to learn Padawan"
elif comp - user == 3 or comp - user == -3:
    msg = "Youngling, your time will come"
else:
    msg = "Keep working hard in the service corps"

print(msg)
