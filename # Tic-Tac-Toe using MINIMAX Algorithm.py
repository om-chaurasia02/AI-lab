# Tic-Tac-Toe using MINIMAX Algorithm
# Human Player  : X
# Computer       : O

# --------------------------------------------------
# Display the board
# --------------------------------------------------
def display_board(board):
    print()
    for row in board:
        print(" ".join(row))
    print()


# --------------------------------------------------
# Check whether a player has won
# --------------------------------------------------
def check_winner(board, player):

    # Check rows
    for row in board:
        if row[0] == player and row[1] == player and row[2] == player:
            return True

    # Check columns
    for col in range(3):
        if (board[0][col] == player and
                board[1][col] == player and
                board[2][col] == player):
            return True

    # Check diagonals
    if (board[0][0] == player and
            board[1][1] == player and
            board[2][2] == player):
        return True

    if (board[0][2] == player and
            board[1][1] == player and
            board[2][0] == player):
        return True

    return False


# --------------------------------------------------
# Check whether board is full
# --------------------------------------------------
def is_full(board):

    for row in board:
        for cell in row:
            if cell == "_":
                return False

    return True


# --------------------------------------------------
# MINIMAX Algorithm
# --------------------------------------------------
def minimax(board, maximizing):

    # Computer wins
    if check_winner(board, "O"):
        return 1

    # Human wins
    if check_winner(board, "X"):
        return -1

    # Draw
    if is_full(board):
        return 0

    # Computer's turn - MAX
    if maximizing:

        best_score = -1000

        for i in range(3):
            for j in range(3):

                if board[i][j] == "_":

                    board[i][j] = "O"

                    score = minimax(board, False)

                    board[i][j] = "_"

                    best_score = max(best_score, score)

        return best_score

    # Human's turn - MIN
    else:

        best_score = 1000

        for i in range(3):
            for j in range(3):

                if board[i][j] == "_":

                    board[i][j] = "X"

                    score = minimax(board, True)

                    board[i][j] = "_"

                    best_score = min(best_score, score)

        return best_score


# --------------------------------------------------
# Find the best move for computer
# --------------------------------------------------
def computer_move(board):

    best_score = -1000
    best_move = None

    for i in range(3):
        for j in range(3):

            if board[i][j] == "_":

                board[i][j] = "O"

                score = minimax(board, False)

                board[i][j] = "_"

                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    return best_move


# --------------------------------------------------
# Main Game
# --------------------------------------------------
def play_game():

    # Create empty 3 x 3 board
    board = [
        ["_", "_", "_"],
        ["_", "_", "_"],
        ["_", "_", "_"]
    ]

    print("===================================")
    print("     TIC-TAC-TOE USING MINIMAX")
    print("===================================")
    print("Human Player   : X")
    print("Computer       : O")
    print("Enter row and column from 1 to 3")

    display_board(board)

    while True:

        # ------------------------------------------
        # Human Move
        # ------------------------------------------
        while True:

            try:
                row, col = map(
                    int,
                    input("Enter row and column: ").split()
                )

                row -= 1
                col -= 1

                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid position! Enter values from 1 to 3.")
                    continue

                if board[row][col] != "_":
                    print("Position already occupied! Try again.")
                    continue

                break

            except ValueError:
                print("Please enter two numbers.")

        board[row][col] = "X"

        print("\nAfter Human Move:")
        display_board(board)

        # Check human win
        if check_winner(board, "X"):
            print("Human Player Wins")
            break

        # Check draw
        if is_full(board):
            print("Game Draw")
            break

        # ------------------------------------------
        # Computer Move using MINIMAX
        # ------------------------------------------
        move = computer_move(board)

        if move is not None:
            row, col = move
            board[row][col] = "O"

        print("Computer Move:")
        display_board(board)

        # Check computer win
        if check_winner(board, "O"):
            print("Computer Wins")
            break

        # Check draw
        if is_full(board):
            print("Game Draw")
            break


# --------------------------------------------------
# Start the program
# --------------------------------------------------
if __name__ == "__main__":
    play_game()
