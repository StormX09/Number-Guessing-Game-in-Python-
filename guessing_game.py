import random
import time

# Store high scores (per difficulty)
high_scores = {
    "easy": None,
    "medium": None,
    "hard": None
}

def get_attempts(choice):
    if choice == "1":
        return "easy", 10
    elif choice == "2":
        return "medium", 5
    elif choice == "3":
        return "hard", 3
    else:
        return None, 0

def give_hint(number, guess):
    diff = abs(number - guess)
    if diff <= 5:
        return "Very close!"
    elif diff <= 15:
        return "Close!"
    else:
        return "Far away!"

def play_game():
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")

    # Difficulty selection
    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    choice = input("Enter your choice: ")
    difficulty, chances = get_attempts(choice)

    if not difficulty:
        print("Invalid choice. Defaulting to Medium.")
        difficulty, chances = "medium", 5

    print(f"\nGreat! You have selected the {difficulty.capitalize()} difficulty level.")
    print("Let's start the game!")

    number = random.randint(1, 100)
    attempts = 0

    start_time = time.time()

    while attempts < chances:
        try:
            guess = int(input("\nEnter your guess: "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        attempts += 1

        if guess == number:
            end_time = time.time()
            total_time = round(end_time - start_time, 2)

            print(f"\nCongratulations! You guessed the correct number in {attempts} attempts.")
            print(f"Time taken: {total_time} seconds")

            # Update high score
            if high_scores[difficulty] is None or attempts < high_scores[difficulty]:
                high_scores[difficulty] = attempts
                print("New High Score!")

            return

        elif guess > number:
            print("Incorrect! The number is less than", guess)
        else:
            print("Incorrect! The number is greater than", guess)

        # Hint system
        print("Hint:", give_hint(number, guess))

        remaining = chances - attempts
        print(f"Attempts left: {remaining}")

    print(f"\n Game Over! The correct number was {number}.")

def show_high_scores():
    print("\n High Scores:")
    for level, score in high_scores.items():
        if score:
            print(f"{level.capitalize()}: {score} attempts")
        else:
            print(f"{level.capitalize()}: No score yet")

def main():
    while True:
        play_game()
        show_high_scores()

        replay = input("\nDo you want to play again? (y/n): ").lower()
        if replay != "y":
            print("\nThanks for playing!")
            break

if __name__ == "__main__":
    main()
