# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a command-line Hangman game in Python that practices string manipulation, loops, conditionals, and handling user input. Students will implement game flow, word selection, and win/lose logic.

## 📝 Tasks

### 🛠️ Implement Hangman Game

#### Description
Using the provided `starter-code.py` as a starting point, implement a playable Hangman game that randomly selects a secret word and lets a player guess letters until they win or run out of attempts.

#### Requirements
Completed program should:

- Randomly select a word from a predefined list inside the program or from a file.
- Prompt the player to guess single letters and update the displayed progress (e.g. `_ a _ _ e`).
- Track and display the number of incorrect attempts remaining.
- Prevent repeated guesses from counting against the player and inform the player of previously guessed letters.
- End the game when the word is fully guessed (win) or when attempts are exhausted (lose), showing an appropriate message and the secret word.
- Keep the code modular: separate logic for word selection, game state updates, and user interaction into functions.

#### Example session

```
Welcome to Hangman!
Word: _ _ _ _ _
Guesses left: 6
Enter a letter: a
Good guess! Word: _ a _ _ _
```

### 🛠️ Optional Enhancements

#### Description
Add one or more of the following to extend the assignment for extra credit.

#### Requirements

- Add difficulty levels that change the allowed attempts or word list.
- Persist a small scoreboard of wins/losses in a local file.
- Support multi-word phrases and show spaces appropriately.

