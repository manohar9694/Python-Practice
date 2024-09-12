# Function to display the Tic-Tac-Toe board
def display_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

# Function to check for a win
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check for a tie
def check_tie(board):
    return all([spot != " " for row in board for spot in row])

# Main game function
def play_tic_tac_toe():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    # Game loop
    while True:
        display_board(board)
        
        # Get player's move
        row = int(input(f"Player {current_player}, enter row (0, 1, 2): "))
        col = int(input(f"Player {current_player}, enter column (0, 1, 2): "))
        
        # Check if the move is valid
        if board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("This spot is already taken. Try again.")
            continue

        # Check for a win or tie
        if check_winner(board, current_player):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        elif check_tie(board):
            display_board(board)
            print("It's a tie!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Start the game
play_tic_tac_toe()
