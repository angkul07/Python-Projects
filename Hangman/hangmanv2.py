import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)
    while '-' in words or ' ' in words:
        word = random.choice(words)

    return word.upper()
    
def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 7

    while len(word_letters)>0 and lives > 0:

        # letters used
        print(f"You have {lives} left. You have used these letter: ", ' '.join(used_letters))

        # Current letter
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))
        
        user_letter = input('Guess the letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1

        elif(user_letter in used_letters):
            print("Try again. You have already use that letter.")

        else:
            print("Invalid letter")
        
    if(lives == 0):
        print("Sorry you died. The correct word is: ", word)
    else:
        print(f"Yayy!! You guess the word {word} !!")
    
hangman()

    
