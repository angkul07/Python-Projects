import random
from playsound import playsound

roll = input("Hit the enter to roll the dice: ")
# Adding sound using playsound when the dice roll
playsound('dice.mp3')
number = [1, 2, 3, 4, 5, 6]
print(f"You got the number: {random.choice(number)}")

# we can also use random.randint(1,6).
