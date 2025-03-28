import random


def number_guessing_game():
    print("Welcome to Mimz Guess Game!")

    # Select difficulty level
    print("Choose a difficulty level:")
    print("1. Easy (1-10, 5 attempts)")
    print("2. Medium (1-25, 3 attempts)")
    print("3. Hard (1-50, 2 attempts)")

    try:
        choice = int(input("Enter 1, 2, or 3: "))

        if choice == 1:
            number = random.randint(1, 10)
            max_attempts = 5
        elif choice == 2:
            number = random.randint(1, 25)
            max_attempts = 3
        elif choice == 3:
            number = random.randint(1, 50)
            max_attempts = 2
        else:
            print("Invalid choice! Defaulting to Medium difficulty.")
            number = random.randint(1, 25)
            max_attempts = 3

        attempts = 0
        print("\nThinking of a number... Try to guess it!")

        while attempts < max_attempts:
            try:
                guessed_number = int(input(f"Attempt {attempts + 1}/{max_attempts}: Guess the number\n"))
                attempts += 1

                if guessed_number < number:
                    print(f"Your guess is too low!")
                elif guessed_number > number:
                    print(f"Your guess is too high!")
                else:
                    print(f"Congratulations! You guessed the number in {attempts} attempts")
                    return
            except ValueError:
                print("Invalid input. Please enter a number.")

        print(f"😞 Sorry! You've used all {max_attempts} attempts. The correct number was {number}.")
    except ValueError:
        print("❌ Invalid input. Restart the game and enter a valid choice.")


number_guessing_game()
