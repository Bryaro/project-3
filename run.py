import random

def create_board():
    """
    function for creating Tic-Tac_Toe table/board
    Return a 3x3 Tic-Tac-Toe board numbered from 1 to 9.
    Each cell of the grid is filled with a number, starting from 1 in the
    top-left cell and ending with 9 in the bottom-right cell.
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
print("Table/board for Tic-Tac-Toe")


def add_list_on_list():
    """
    add lists on eachother 
    so it represent a 3x3 grid 
    to look more like Tic-Tac-Toe board
    """
    board = create_board()
    for row in board:
        print(row)

list_block = add_list_on_list()
print(list_block)