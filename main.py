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
    """Clears the console screen based on the operating system."""
    os.system("cls" if os.name == "nt" else "clear")

def start_game():
    """
    Starts the number guessing game.
    - The user guesses a number between 1 and 100.
    - Tracks number of attempts and stores all guesses.
    - Clears the screen between guesses for a clean interface.
    """
    print("~~~~~~~~~~ Number Guessing Game ~~~~~~~~~~\nA number between 1 and 100 has been selected. Can you guess it?")
    input("Press Enter to start...")
    clear_screen()

    number = random.randint(1, 100)
    guess = None
    attempts = 0
    guesses = []  # List to store all user guesses

    while guess != number:
        try:
            guess = int(input("Please enter your guess (1–100): "))

            if guess < 1 or guess > 100:
                clear_screen()
                print("❗ Please enter a number between 1 and 100.\n")
                print("📜 Your guesses so far:", guesses)
                print("-----------------------------------------")
                continue

            attempts += 1
            guesses.append(guess)
            clear_screen()

            if guess < number:
                print("🔻 Your guess is lower than the number.")
            elif guess > number:
                print("🔺 Your guess is higher than the number.")
            else:
                print(f"🎉 You got it right in {attempts} attempts!")

            print(f"📊 Attempt #{attempts}")
            print("📜 Your guesses so far:", guesses)
            print("-----------------------------------------")

        except ValueError:
            clear_screen()
            print("❗ Only numeric input is allowed. Please try again.\n")
            print("📜 Your guesses so far:", guesses)
            print("-----------------------------------------")

# Run the game in a loop with replay option
if __name__ == "__main__":
    while True:
        start_game()
        choice = input("Would you like to play again? (y/n): ").strip().lower()
        if choice != 'y':
            print("Thanks for playing! 👋")
            break
        clear_screen()
