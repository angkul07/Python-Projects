import random

print("Replace the [] with the most suitable words you feel.")

a = "[Name] had a pet [animal] named [pet_name]. One day, they went on a(n) [adjective1] adventure together. [Name] decided to cook [food] for dinner, but they accidentally added [weird_ingredient]. The meal turned out [adjective2]!"

b = "On a sunny [day_of_the_week], [Name] went to the [noun] and found a mysterious [object]. They decided to take it home and soon discovered that it had the power to [verb] anything!"

madlibList = [a, b]

list = random.choice(madlibList)
print(list)

if list == a:
    Name = input("Name: ")
    animal = input("Animal: ")
    pet_name = input("Pet name: ")
    adjective1 = input("Adjective 1: ")
    Name_s = input("Name: ")
    food = input("Food: ")
    weird_ingredient = input("Weird Ingredient: ")
    adjective2 = input("Adjective 2: ")

    print(f"{Name} had a pet {animal} named {pet_name}. One day, they went on a(n) {adjective1} adventure together. {Name} decided to cook {food} for dinner, but they accidentally added {weird_ingredient}. The meal turned out {adjective2}!")

elif list == b:
    day_of_the_week = input("Day of the week: ")
    Name = input("Name: ")
    noun = input("Noun: ")
    object = input("Object: ")
    verb = input("Verb: ")

    print(f"On a sunny {day_of_the_week}, {Name} went to the {noun} and found a mysterious {object}. They decided to take it home and soon discovered that it had the power to {verb} anything!")





