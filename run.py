import random

def create_board():
    """
    Create and return a 3x3 Tic-Tac-Toe board numbered from 1 to 9.
    Each cell of the grid is filled with a number, starting from 1 in the
    top-left cell and ending with 9 in the bottom-right cell.
    Returns:
    list of lists: A 3x3 grid representing the Tic-Tac-Toe board,
    with each cell numbered from 1 to 9.
    """
    board = []
    cell_number = 1
    for i in range(3):
        row = []
        for j in range(3):
            row.append(cell_number)
            cell_number += 1
        board.append(row)
    return board
print("\nTable/board for Tic-Tac-Toe\n")


def print_board(board):
    """
    Display/Print to terminal
    each cell is divided with " | "
    each row is rivided with "--" + "+-" + "--" + "+--"
    which will turn to a more visible display to user
    Display will be more identical to Tic-Tac-Toe with each cell representing a number
    and each number is representing a cell
    """
    for row in board:
        print(" | ".join(str(cell) for cell in row))
        print("--" + "+-" + "--" + "+--")

def player_turn(board):
    """
    Create player turn
    lets player type number from 1-9
    raise error if player chose incorrect or already chosen data
    this will run in while loop till player/user chosen correct data
    """
    while True:
        print("\nplayer turn working\n")
        try:
            turn = int(input("Enter a number 1-9:"))
            row = (turn - 1) // 3 
            col = (turn - 1) % 3
            if board[row][col] == turn:
                board[row][col] = "X"
                break
            else:
                print("\ncell already taken. Try again\n")
        except (ValueError, IndexError):
            print("you typed invalid data, you need to type only number bewteen 1-9\n")

def computer_turn(board):
    """
    Create computer turn
    This function randomly selects a cell on the board for the computer's turn.
    If the selected cell is unoccupied, it marks the cell with 'O'.
    """
    while True:
            turn = random.randint(1, 9)
            row = (turn - 1) // 3 
            col = (turn - 1) % 3
            if board[row][col] == turn:
                board[row][col] = "O"
                break

def check_winner(board, player):
    """
    Check for winner (computer or user).
    Args board for the current table, and player(the computer or the user)
    """
    for i in range(3):
        if board[i][0] == player and board[i][1] == player and board[i][2] == player:
            return True
        if board[0][i] == player and board[1][i] == player and board[2][i] == player:
            return True
    if board[0][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    if board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return True
    

def main():
    """
    Runs the main function for the Tic-Tac-Toe game.
    """
    board = create_board()
    print("\n Initial Tic Tac Toe board\n")
    print_board(board)

    while True:
        player_turn(board)
        print("\nBoard after Player turn")
        print_board(board)
        if check_winner(board, "X"):
            print("\n You Win!")


main()