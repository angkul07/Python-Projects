import random

words = "abcdefghijklmnopqrstuvwxyz"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()-_=+|[]`~/?.,><:;"

digit = int(input("How many characters: "))

password = []

for i in range(1, digit+1):
    ra1 = random.choice(words)
    ra2 = random.choice(capital)
    ra3 = random.choice(numbers)
    ra4 = random.choice(symbols)
    password.append(ra1)
    password.append(ra2)
    password.append(ra3)
    password.append(ra4)

print("Your Password: ")
print("".join(password))
