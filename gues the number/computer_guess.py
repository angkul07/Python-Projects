import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    
    while(feedback != 'c'):
        if(low != high):
            guess = random.randint(low, high)
        else:
            guess = low

        feedback = input(f"Is {guess} to high(H) or to low(L) or correct(c)").lower()
        if(feedback == 'h'):
            guess = guess - 1
        elif(feedback == 'l'):
            guess = guess + 1

    print(f"Yayy! Computer guess number {guess}, correctly.")

computer_guess(10)