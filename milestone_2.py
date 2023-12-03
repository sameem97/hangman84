import random

word_list = ["Pineapple", "Mango", "Blueberries", "Kiwi", "Orange"]

word = random.choice(word_list)


while True:
    guess = input("Please enter a single letter")
    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
        break
    else:
        print("Oops! That is not a valid input. Please try again!")
        continue