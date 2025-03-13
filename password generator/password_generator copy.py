import random

words = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+|[]`~/?.,><:;"

digit = int(input("How many characters: "))

password = []

for i in range(1, digit+1):
    ra1 = random.choice(words)
    password.append(ra1)

print("Your Password: ")
print("".join(password))
