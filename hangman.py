import random
from typing import List
from utils.variables import word_list

class Hangman:
    def __init__(self, word_list: List[str]) -> None:
        self.word_list = word_list
        self.word: str = random.choice(word_list)
        self.word_guessed: List[str] = ["_" for character in self.word]
        self.num_letters: int = len(set(self.word))
        self.num_lives: int = 5
        self.list_of_guesses: List[str] = []

    def __check_guess(self, guess: str):
        guess = guess.lower()
        if guess in self.word:
            print(f"Good guess! {guess} is in the word.")
            for letter in self.word:
                if letter == guess:
                    index = self.word.index(letter)
                    self.word_guessed[index] = guess
            print(self.word_guessed)
            self.num_letters -= 1
        else:
            print(f"Sorry. {guess} is not in the word. Try again.")
            self.num_lives -= 1
            print(f"You have {self.num_lives} lives left.")
    
    def ask_for_input(self):
        while True:
            guess = input("Please guess a letter")
            if not len(guess) == 1 and not guess.isalpha():
                print("Invalid letter. Please enter a single alphabetical character.")
                continue
            elif guess in self.list_of_guesses:
                print(f"You already tried that letter!")
            else:
                self.__check_guess(guess)
                self.list_of_guesses.append(guess)

if __name__ == "__main__":
    game = Hangman(word_list)
    game.ask_for_input()



