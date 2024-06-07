# GUESS A WORD

Guess a Word is a Python terminal game where players guess letters to reveal a hidden word from a chosen category. The game runs in the Code Institute mock terminal on Heroku and provides a fun and challenging word-guessing experience.

![Responsice Mockup](https://github.com/Agnesgran/GuessAWord/blob/main/assets/images/mockup.png)

## How to play

1. **Choose a category**: Select from the available categories: fruits, animals, or colors.
2. **Guess letters**: Enter one letter at a time to reveal the hidden word.
3. **Attempts**: You have six attempts to guess the word correctly.
4. **Scoring**: Each correct guess reveals the letter in the word. Incorrect guesses reduce the number of attempts left.
5. **End of Game**: The game ends when you guess the word or run out of attempts.
6. **Play Again**: After each round, view your score and choose to play again if desired.

## Features

### Existing Features
- **Category Selection**
  - Players can choose from three categories: fruits, animals, or colors.
  ![Category Selection](https://github.com/Agnesgran/GuessAWord/blob/main/assets/images/categoryselection.png)
- **Word Guessing**
  - Players guess letters to reveal the hidden word.
  ![Word Guessing](https://github.com/Agnesgran/GuessAWord/blob/main/assets/images/wordguessing.png)
- **Attempts Tracking**
  - Players have six attempts to guess the word.
  ![Attempts Tracking]()
- **Feedback on Guesses**
  - Correct guesses reveal letters in the word.
  - Incorrect guesses are counted against the player.
  ![Feedback on Guesses]()
- **Score Display**
  - The game displays the number of wins and losses.
  ![Score Display]()
- **Play Again Option**
  - Players can choose to play another round after the game ends.
  ![Play Again Option]()

### Input Validation and Error Checking
- **Single Letter Input**
  - Ensures players enter only one letter at a time.
  ![Single Letter Input]()
- **Repeated Guesses**
  - Prevents players from guessing the same letter more than once.
  ![Repeated Guesses]()
- **Catergory Choice**
  - Ensures players enter one of the given category choices.
  ![Catergory Choice]()

## Data Model

The game uses simple lists and strings to manage the game state. It maintains:
- **Categories**: A dictionary of categories and corresponding words.
- **Guessed Letters**: A list to track letters guessed by the player.
- **Attempts**: An integer to track remaining attempts.
- **Score**: Two integers to track wins and losses.

## Testing

The game has been manually tested by:
- **Validating Input Handling**
  - Tested for non-alphabetical input, multiple letters, and repeated guesses.
- **Gameplay Flow**
  - Ensured the game correctly tracks and displays the game state, attempts, and score.

## Bugs

### Solved Bugs
- **Input Validation**
  - **Issue**: The game previously accepted multiple letters at a time and allowed repeated guesses of the same letter.
  - **Resolution**: Implemented checks to ensure that only single alphabetical characters are accepted as valid input. Added a condition to check if the guessed letter had already been guessed, providing appropriate feedback and not decrementing the attempts.

### Remaining Bugs
- No known bugs remaining.

## Validator Testing

- **PEP8**
  - No errors were returned from https://pep8ci.herokuapp.com/# 

## Deployment

This project was deployed using the Code Institute's mock terminal for Heroku.

- Steps for deployment:
  - Fork or clone this repository
  - Create a new Heroku app
  - Set the buildpacks to `Python` and `NodeJS` in that order
  - Link the Heroku app to the repository
  - Click on Deploy

## Credits

- https://www.w3schools.com/python/python_try_except.asp.
- https://www.w3schools.com/python/ref_random_choice.asp.
- https://www.w3schools.com/.
- Code Institute for the PEP8 Linter.
- Code Institute for the deployment terminal.
- Code Institute Python Essentials.
- Code Institute Python Functions & Objects Oriented Programming.
- Code Institute Python I/O Exception Handling. 

