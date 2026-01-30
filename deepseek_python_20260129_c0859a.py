import random

def print_board(board):
    """Prints the Tic Tac Toe board."""
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    """Checks if the given player has won."""
    # Check rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):  # Rows
            return True
        if all([board[j][i] == player for j in range(3)]):  # Columns
            return True
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:  # Main diagonal
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:  # Anti-diagonal
        return True
    return False

def is_board_full(board):
    """Checks if the board is full."""
    for row in board:
        if " " in row:
            return False
    return True

def get_player_move(board):
    """Gets and validates the player's move."""
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if 0 <= move <= 8 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Try again.")
        except (ValueError, IndexError):
            print("Please enter a number between 1 and 9.")

def get_bot_move(board, bot_char, player_char):
    """Simple bot logic: tries to win, block, or move randomly."""
    # 1. Try to win
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = bot_char
                if check_winner(board, bot_char):
                    board[i][j] = " "
                    return i, j
                board[i][j] = " "
    
    # 2. Try to block player's win
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = player_char
                if check_winner(board, player_char):
                    board[i][j] = " "
                    return i, j
                board[i][j] = " "
    
    # 3. Try to take center if free
    if board[1][1] == " ":
        return 1, 1
    
    # 4. Try corners
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    random.shuffle(corners)
    for corner in corners:
        if board[corner[0]][corner[1]] == " ":
            return corner
    
    # 5. Random move
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]
    return random.choice(empty_cells)

def play_game():
    """Main game loop."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_char = "X"
    bot_char = "O"
    
    print("Welcome to Tic Tac Toe vs Bot!")
    print("Positions are numbered 1-9 (like a phone keypad):")
    print(" 1 | 2 | 3 ")
    print("-----------")
    print(" 4 | 5 | 6 ")
    print("-----------")
    print(" 7 | 8 | 9 ")
    
    # Randomly decide who goes first
    player_turn = random.choice([True, False])
    if player_turn:
        print("\nYou go first (X).")
    else:
        print("\nBot goes first (O).")
    
    while True:
        print_board(board)
        
        if player_turn:
            # Player's turn
            row, col = get_player_move(board)
            board[row][col] = player_char
            
            if check_winner(board, player_char):
                print_board(board)
                print("🎉 You win!")
                break
        else:
            # Bot's turn
            print("Bot is thinking...")
            row, col = get_bot_move(board, bot_char, player_char)
            board[row][col] = bot_char
            print(f"Bot plays at position {row * 3 + col + 1}")
            
            if check_winner(board, bot_char):
                print_board(board)
                print("🤖 Bot wins!")
                break
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        # Switch turns
        player_turn = not player_turn
    
    play_again = input("\nPlay again? (y/n): ").lower()
    if play_again == "y":
        play_game()
    else:
        print("Thanks for playing!")

# Start the game
if __name__ == "__main__":
    play_game()