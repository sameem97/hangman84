"""Module for hangman game."""
import random
import sys
from typing import List
from env_vars import word_list


class Hangman:
	"""Class to represent Hangman object."""

	def __init__(self, word_list: List[str]) -> None:
		self.word_list = word_list
		self.word: str = random.choice(word_list).lower()
		self.word_guessed: List[str] = ["_" for character in self.word]
		self.num_letters: int = len(set(self.word))
		self.num_lives: int = 5
		self.list_of_guesses: List[str] = []

	def __update_word_guessed(self, guess: str):
		"""for a correct guess, update the word with the letter guessed"""
		current_index = 0
		for letter in self.word:
			if letter == guess:
				current_index = self.word.index(letter, current_index)
				self.word_guessed[current_index] = guess
				current_index += 1

	def __check_guess(self, guess: str):
		"""Check if the guess is correct.
        If so, update the word and reduce num_letters.
        Otherwise reduce num_lives"""
		if guess in self.word:
			print(f"Good guess! {guess} is in the word.")
			self.__update_word_guessed(guess)
			print(self.word_guessed)
			self.num_letters -= 1
			if self.num_letters == 0:
				print("You have won! Congrats!")
				sys.exit(-1)
		else:
			print(f"Sorry. {guess} is not in the word. Try again.")
			self.num_lives -= 1
			if self.num_lives == 0:
				print("You have ran out of lives. Better luck next time!")
				sys.exit(-1)
			else:
				print(f"You have {self.num_lives} lives left.")

	def ask_for_input(self):
		"""get user input and check if it is single character alphabet.
          If so, then proceed with check_guess and append guess to list_of_guesses."""
		while True:
			guess = input("Please guess a letter").lower()
			if not len(guess) == 1 or not guess.isalpha():
				print("Invalid input. Please enter a single alphabetical character.")
			elif guess in self.list_of_guesses:
				print(f"You already tried that letter!")
			else:
				self.__check_guess(guess)
				self.list_of_guesses.append(guess)


if __name__ == "__main__":
	game = Hangman(word_list)
	game.ask_for_input()
