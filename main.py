"""
Number Guessing Game
-----------------------
This console-based Python game generates a random number between 1 and 100.
The player must guess the number, and the game provides feedback after each guess.
All guesses are stored and displayed after each turn. The screen is cleared to keep the UI clean.
"""

import random
import os

def clear_screen():
    #Clears the console screen based on the operating system.
    os.system("cls" if os.name == "nt" else "clear")


def start_game():
    """
    Starts the number guessing game.
    - The user guesses a number between 1 and 100.
    - Tracks number of attempts and stores all guesses.
    - Clears the screen between guesses for a clean interface.
    """
    print("~~~~~~~~~~ Number Guessing Game ~~~~~~~~~~")
    print("A number between 1 and 100 has been selected, Can You Guess it?")
    input("Press Enter to start...")
    clear_screen()

    number = random.randint(1, 100)
    guess = None
    attempts = 0
    guesses = []  # List to store all user guesses

    while guess != number:
        try:
            guess = int(input("Please enter your guess (1-100): "))
            attempts += 1
            guesses.append(guess)

            clear_screen()

            if guess < number:
                print("🔻 Your guess is lower than the number.")
            elif guess > number:
                print("🔺 Your guess is higher than the number.")
            else:
                print(f"🎉 You got it right in {attempts} attempts!")

            # Display all previous guesses
            print("📜 Your guesses so far:", guesses)
            print("-----------------------------------------")

        except ValueError:
            clear_screen()
            print("❗ Only numeric input is allowed. Please try again.\n")
            print("📜 Your guesses so far:", guesses)
            print("-----------------------------------------")

# Run the game
if __name__ == "__main__":
    start_game()