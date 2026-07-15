# Number Guessing Game (CLI)

A simple and interactive **Command-Line Number Guessing Game** built in Python. The computer randomly selects a number between 1 and 100, and the player must guess it within a limited number of attempts based on the selected difficulty level.

---

## Features

* CLI-based interactive gameplay
* Random number generation (1–100)
* Difficulty levels:

  * Easy (10 attempts)
  * Medium (5 attempts)
  * Hard (3 attempts)
    
* Feedback after each guess (higher/lower)
* Hint system based on how close your guess is
* Timer to track how long you take
* Replay option (play multiple rounds)
* High score tracking per difficulty

---

## How It Works

1. The game starts with a welcome message and instructions.
2. The player selects a difficulty level.
3. The system randomly generates a number between 1 and 100.
4. The player inputs guesses:

   * If correct → Player wins
   * If incorrect → The game gives hints (higher/lower + closeness)
     
5. The game ends when:

   * The player guesses correctly, OR
   * The player runs out of attempts
6. Player can choose to play again.

---

## How to Run

1. Clone or download this repository
2. Navigate to the project folder
3. Run the script:

```bash
python guessing_game.py
```

---

## Sample Gameplay

```
Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.

Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)

Enter your choice: 2

Great! You have selected the Medium difficulty level.
Let's start the game!

Enter your guess: 50
Incorrect! The number is less than 50.

Enter your guess: 25
Incorrect! The number is greater than 25.

Enter your guess: 30
Congratulations! You guessed the correct number in 3 attempts.
```

---

## License

This project is open-source and free to use.

---

## Project URL

https://github.com/StormX09/Number-Guessing-Game-in-Python-.git

---
