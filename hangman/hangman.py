import random
import string
from words import words
from visuals import lives_visual_dict


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

    lives = 7;

    while len(req_letter) > 0 and lives > 0:
        print("You have used following letters: ", ' '.join(used_letter))
        print(f'You have {lives} lives left.')

        word_list = [letter if letter in used_letter else '-' for letter in word]
        print(lives_visual_dict[lives])
        print(f"Current words: ", ' '.join(word_list))

        
        user_letter = input("Guess the letter: ").upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in req_letter:
                req_letter.remove(user_letter)

            else:
                lives = lives - 1
                print('\nYour letter,', user_letter, 'is not in the word.')


        elif user_letter in used_letter:
            print("\nYou have already used that letter. Guess another letter.")

        else:
            print("Not a valid letter")

    if(lives == 0):
        print("Sorry, you couldn't guess the word. The correct word was:", word)
    else:
        print(f"YAYY!! you have guessed the word {word} !!")



hangman()


        





        
