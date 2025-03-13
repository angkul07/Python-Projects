import random

words = "abcdefghijklmnopqrstuvwxyz"
capital = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*()-_=+|[]`~/?.,><:;"

allchar = f"{words}+{capital}+{numbers}+{symbols}"

digit = int(input("Enter your desired length of password: "))

password = []

for i in range(1, digit+1):
    ra = random.choice(allchar)
    password.append(ra)
    

print("Your Password: ")
print("".join(password))
print("Thanks for using. Hope you generate a strong passowrd :)")