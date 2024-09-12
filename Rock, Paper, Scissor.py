import random

# Choices available
choices = ['rock', 'paper', 'scissors']

# Function to determine the winner
def find_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        return "You win!"
    else:
        return "You lose!"

# Main game loop
while True:
    # Get user input and computer's random choice
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    computer_choice = random.choice(choices)

    # Show choices
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    # Find and display winner
    result = find_winner(user_choice, computer_choice)
    print(result)

    # Ask if the user wants to play again
    play_again = input("\nPlay again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Goodbye!")
        break





