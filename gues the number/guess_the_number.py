import random

"""
Version 1.0 of random number

random_number = random.randrange(1,5)
user = int(input())
if user == random_number:
    print("Yayyyyy")
else:
    print("Whoops! Try again")
print(random_number)
"""

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while(guess != random_number):
        guess = int(input(f"Chose any number between 1 and {x}: "))
        if guess < random_number:
            print("Whoops! Try again. Too low")
        elif guess > random_number:
            print("Whoops! Try again. Too high")

    print("Yayyy!!!!! You guess the correct number.")

guess(12)
    