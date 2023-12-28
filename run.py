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
print("table/board for Tic Tac&\n")

board = create_board()
for row in board:
    print(row)