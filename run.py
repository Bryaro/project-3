import random

def create_board():
    """
    function for creating Tic-Tac_Toe table/board
    """
    board = []
    
    for i in range(3):
        row = []
        for j in range(3):
            row.append(" ")
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