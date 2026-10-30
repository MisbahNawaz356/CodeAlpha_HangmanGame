
import random

# List of 5 predefined words
words = ["python", "computer", "program", "keyboard", "developer"]

# Select a random word
secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_attempts = 6

print("================================")
print("       WELCOME TO HANGMAN")
print("================================")

while wrong_guesses < max_attempts:
    # Display the word with hidden letters
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses left:", max_attempts - wrong_guesses)

    # Check whether the player has won
    if all(letter in guessed_letters for letter in secret_word):
        print("Congratulations! You won!")
        print("The word was:", secret_word)
        break

    guess = input("Guess one letter: ").lower().strip()

    # Validate the user's input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!")
    else:
        wrong_guesses += 1
        print("Wrong guess!")

else:
    print("\nGame over! You lost.")
    print("The word was:", secret_word)

print("Thanks for playing!")
