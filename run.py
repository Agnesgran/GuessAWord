import random


def get_word():
    """
    Selects a random word from a chosen category.
    """
    categories = {
        "fruits": ["apple", "banana", "cherry", "date", "fig"],
        "animals": ["dog", "cat", "elephant", "giraffe", "hippopotamus"],
        "colors": ["red", "blue", "green", "yellow", "purple"]
     }

    while True:
        # Display available categories
        print("Choose a category: ", ', '.join(categories.keys()))
        category = input().lower()

        if category in categories:
            # Return a random word from the chosen category
            return random.choice(categories[category])
        else:
            print("Uh-oh! That category's not on the list."
                  "Try one of the given choices.")


def guess_a_word():
    """
    Main function to run the game.
    Manages game state, handles user input, and controls game flow.
    """
    wins = 0
    losses = 0

    while True:
        word = get_word()
        guessed_letters = []
        attempts = 6
        print("Welcome to Guess A Word! Guess the word one letter at a time. "
              "But be careful, you only have 6 attempts!")
        while attempts > 0:
            progress_update(word, guessed_letters)

            # Prompt the user to guess a letter
            guess = input("Guess a letter:\n").lower().strip()

            if not guess.isalpha() or len(guess) != 1:
                print("Oops! Just one letter at a time, please!")
                continue

            if guess in guessed_letters:
                print("Déjà vu! You’ve already picked that one.")
            elif guess in word:
                guessed_letters.append(guess)
                print("Nice job!")
            else:
                guessed_letters.append(guess)
                attempts -= 1
                print("Bummer! That's not it. Tries left:", attempts)

            if all(letter in guessed_letters for letter in word):
                print("Woohoo! You figured out the word:", word)
                wins += 1
                break
        else:
            print("Oh snap! Out of tries. The word was:", word)
            losses += 1

        display_score(wins, losses)
        if not play_again():
            print("Thanks for the fun! Come back soon!")
            break


def progress_update(word, guessed_letters):
    """
    Displays the current state of the game,
    showing guessed letters and blanks for unguessed letters
    """
    display = ''.join([
        letter if letter in guessed_letters else '_' for letter in word])
    print("Current word: ", display)
    print("Guessed letters: ", ' '.join(guessed_letters))


def display_score(wins, losses):
    """
    Displays the current score of the player.
    """
    print(f"Score: {wins} Wins, {losses} Losses")


def play_again():
    """
    Asks the player if they want to play again.
    """
    while True:
        choice = input("Do you want to play again? (y/n):\n").strip().lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' for Yes or 'n' for No.")


if __name__ == "__main__":
    guess_a_word()
