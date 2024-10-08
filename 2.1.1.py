import random

def main():
    # Generate a random number between 1 and 100
    number = random.randint(1, 100)
    print("Welcome to the Number Guessing Game!")
    print("Guess the number between 1 and 100!")  # Prompt for the user

    while True:  # Loop until the user guesses correctly
        try:
            # User's guess
            guess = int(input("Enter your guess: "))
            difference = abs(guess - number)

            # Provide feedback to the user
            if guess == number:
                print("Congratulations! You've guessed the correct number!")
                break
            elif difference <= 5:
                print("Very Hot!")
            elif difference <= 15:
                print("Hot!")
            elif difference <= 25:
                print("Cool!")
            else:
                print("Cold!")

        except ValueError:  # Handle non-integer inputs
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()  # Calls the main function
