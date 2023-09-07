a = int(input("Enter your 1st number: "))
b = int(input("Enter your 2nd number: "))

calc = input("Enter your desired operator: + - * /: ")

if calc == '+':
    print(a+b)

elif calc == '-':
    print(a-b)

elif calc == '*':
    print(a*b)

elif calc == '/':
    print(a/b)

else:
    print("Sorry this is a very basic simple calcualtor.")




