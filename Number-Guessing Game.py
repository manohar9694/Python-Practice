import random

# Function to play the number guessing game
def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Get user input
            guess = int(input("Guess the number (between 1 and 100): "))
            attempts += 1
            
            # Check if the guess is too low, too high, or correct
            if guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")

# Start the game
number_guessing_game()
