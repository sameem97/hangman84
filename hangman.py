import random
from typing import List
from utils.guess import get_user_guess
from utils.variables import word_list

def main() -> None:
    """Play hangman using a random word from an inputted list of words"""
    word = random.choice(word_list)
    guess = get_user_guess()
    if guess in word:
        print(f"Good guess! {guess} is in the word.")
    else:
        print(f"Sorry. {guess} is not in the word. Try again.")


if __name__ == "__main__":
    main()




