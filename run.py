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
            print("Uh-oh! That category's not on the list. Try one of the given choices.")
    
def guess_a_word():
    """
    Main function to run the game. 
    Manages game state, handles user input, and controls game flow.
    """
    
def progress_update(word, guessed_letters):
    """
    Displays the current state of the game, 
    showing guessed letters and blanks for unguessed letters
    """ 

def display_score(wins, losses):
    """
    Displays the current score of the player.
    """


def play_again():
    """
    Asks the player if they want to play again.
    """



