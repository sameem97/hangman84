import random

word_list = ["Pineapple", "Mango", "Blueberries", "Kiwi", "Orange"]

word = random.choice(word_list)

def get_user_guess() -> str:
    while True:
        guess = input("Please enter a single letter")
        if len(guess) == 1 and guess.isalpha():
            print("Good guess!")
            return guess
        else:
            print("Oops! That is not a valid input. Please try again!")
            continue