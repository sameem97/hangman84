def get_user_guess() -> str:
    while True:
        guess = input("Please guess a letter")
        if len(guess) == 1 and guess.isalpha():
            return guess
        else:
            print("Invalid letter. Please enter a single alphabetical character.")
            continue