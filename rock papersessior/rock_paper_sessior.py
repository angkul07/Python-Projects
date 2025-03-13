import random

def play():
    user = input("What's your choice: 'r' for rock, 's' for sessior, 'p' for paper: ")
    computer = random.choice(['r', 's', 'p'])

    if(user == computer):
        return "Its a tie."
    
    if is_win(user, computer):
        return "You won!"

    return "Try again!"


# s > p, r > s, p > r
def is_win(user, player):
    if(user == 's' and player == 'p') or (user == 'r' and player == 's') \
    or (user == 'p' and player == 'r'):
        return True
    

print(play())
