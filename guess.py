import random

print("This is the number guessing game")
number = random.randint(1, 9)
chances = 0

print("Choose a number between 1-9")

while chances < 5:
    guess = int(input("What is the number you chose:- "))
    if guess == number:
        print("You won!")
        break
    elif guess < number:
        print("Your guess was low; Try again.", guess)

    else:
        print("Your guess was high; Try again", guess)

    chances += 1


    if chances < 5:
        print("Sorry, but you lost. The number was -> ", number)