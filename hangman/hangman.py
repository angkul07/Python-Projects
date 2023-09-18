import random
import string
from words import words


# Let chose a word from list of Words
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    
    return word.upper()


# Taking input from the user
def hangman():
    word = get_valid_word(words)
    req_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()


    while len(req_letter) > 0:
        print("You have used following letters: ", ' '.join(used_letter))

        word_list = [letter if letter in used_letter else '-' for letter in word]
        print(f"Current words: ", ' '.join(word_list))
        
        user_letter = input("Guess the letter: ").upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in req_letter:
                req_letter.remove(user_letter)


        elif user_letter in used_letter:
            print("\nYou have already used that letter. Guess another letter.")

        else:
            print("Not a valid letter")

    print(f"YAYY!! you have guessed the word {word} !!")


hangman()


        





        
