# Anderson Okai
# Added a scoring system that rewards players for guessing longer words, making the game more challenging and fun.
# The program now selects a random word from a predefined list for each game.

import random

word_list = ["mosiah", "helaman", "nephi", "alma", "abinadi", "moroni", "lehi", "sariah"]

def initialize_hint(secret_word):
    return ['_' for _ in secret_word]

def display_hint(hint):
    print("Your hint is:", ' '.join(hint))

def update_hint(secret_word, guess, hint, guess_count):
    for i, (sw, gw) in enumerate(zip(secret_word, guess)):
        if sw == gw:
            hint[i] = gw.upper()
            guess_count += 1  # Increment guess_count only for correct letters
        elif gw in secret_word:
            hint[i] = gw.lower()
    return guess_count

def calculate_score(secret_word, guess_count):
    return (len(secret_word) - guess_count) * 10  # Adjusted score calculation

def play_word_puzzle(secret_word):
    guess_count = 0
    hint = initialize_hint(secret_word)

    print("Welcome to the word guessing game!")

    while '_' in hint:
        display_hint(hint)
        user_guess = input("What is your guess? ").lower()

        if len(user_guess) != len(secret_word):
            print("Sorry, the guess must have the same number of letters as the secret word.")
            continue

        guess_count = update_hint(secret_word, user_guess, hint, guess_count)
        print(f"It took you {guess_count} guesses.")  # Display guess count after each guess

    display_hint(hint)
    score = calculate_score(secret_word, guess_count)
    print(f"Congratulations! You guessed it!\nIt took you {guess_count} guesses.")
    print(f"Your score is: {score} points.")

if __name__ == "__main__":
    secret_word = random.choice(word_list)
    play_word_puzzle(secret_word)







