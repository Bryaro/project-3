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


def add_list_on_list():
    """
    add lists on eachother 
    so it represent a 3x3 grid 
    to look more like Tic-Tac-Toe board
    """
    board = create_board()
    for row in board:
        print(row)

add_list_on_list()


def player_turn():
    """
    Create player turn
    lets player type number from 1-9
    raise error if player chose incorrect or already chosen data
    this will run in while loop till player/user chosen correct data
    """
    print("\nPlayers turn, chose nr fr 1-9\n")
    
player_turn()