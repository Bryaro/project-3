import random
import os


green_color = "\033[92m"
red_color = "\033[91m"
default_color = "\033[0m"


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


def print_board(board):
    """
    Display/Print to terminal
    each cell is divided with "  ┃  "
    each row is divided with "━━╋━━╋━━"
    which will turn to a more visible display to user
    Display will be more identical to Tic-Tac-Toe
    Each cell representing a number
    and each number is representing a cell
    """
    indent = "\t\t"
    row_counter = 0
    print(" ")
    for row in board:
        print(indent + " ┃ ".join(str(cell) for cell in row))
        row_counter += 1  # Increment the row counter after printing each row
        if row_counter < 3:  # Only print separator if it's not the last row
            print(indent + "━" + "━╋━" + "━" + "━╋━━")


def player_turn(board, player_name):
    """
    Create player turn
    lets player type number from 1-9
    raise error if player chose incorrect or already chosen data
    this will run in while loop till player/user chosen correct data
    """
    while True:
        try:
            turn = int(input(
                f"\n     {player_name}'s turn. Enter a number 1-9:\n"))
            row = (turn - 1) // 3
            col = (turn - 1) % 3

            if board[row][col] == turn:
                board[row][col] = "X"
                break
            else:
                print("\ncell already taken. Try again\n")
        except (ValueError, IndexError):
            print("you typed invalid data,"
                  " you need to type only number bewteen 1-9\n")


def computer_turn(board):
    """
    Create computer turn
    This function randomly selects a cell on the board for the computer's turn.
    If the selected cell is unoccupied, it marks the cell with '𝖮'.
    """
    while True:
        turn = random.randint(1, 9)
        row = (turn - 1) // 3
        col = (turn - 1) % 3
        if board[row][col] == turn:
            board[row][col] = "𝖮"
            break


def computer_turn_difficult(board):
    """
    Create difficult computer level
    This function randomly selects a cell on the board for the computer's turn,
    but if the cell 1, and cell 2 is occupied with X,
    and if cell 3 is unoccupied, it occupies the cell 3 with '𝖮'.
    """
    # if (board[0][0] == "X" and
    #         board[0][1] == "X" and
    #         isinstance(board[0][2], int)):
    #     board[0][2] = "𝖮"
    #     return
    for row in board:
        if row.count("X") == 2:
            for i in range(3):
                if isinstance(row[i], int):
                    row[i] = "𝖮"
                    return
    computer_turn(board)


def computer_turn_lvl3(board):
    """
    Create Hard computer level
    this will always occupy the third cell with "𝖮" in the row
    if two other cells in the row are occupied
    """
    for row in board:
        if row.count("X") == 2 or row.count("𝖮"):
            for i in range(3):
                if isinstance(row[i], int):
                    row[i] = "𝖮"
                    return
    computer_turn(board)


def check_winner(board, player):
    """
    Check for winner (computer or user).
    Args board for the current table, and player(the computer or the user)
    """
    for i in range(3):
        if (board[i][0] == player and
                board[i][1] == player and
                board[i][2] == player):
            return True
        if (board[0][i] == player and
                board[1][i] == player and
                board[2][i] == player):
            return True
    # diagonal
    if (board[0][0] == player and
            board[1][1] == player and
            board[2][2] == player):
        return True
    # diagonal
    if (board[2][0] == player and
            board[1][1] == player and
            board[0][2] == player):
        return True
    return False


def check_tie(board):
    """
    Checks for Tie
    """
    cell_count = 0
    for row in board:
        for cell in row:
            if cell == "X" or cell == "𝖮":
                cell_count += 1
    return cell_count == 9


def clear_terminal():
    """
    Clears the terminal window prior to new content.
    Original code from
    http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf
    Recommended to me by Goran Sigeskog
    https://github.com/gorsig
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def game_menu():
    """
    MENU START
    Show rules, play game.
    """
    clear_terminal()
    print(f"{green_color}\n"
          "▒█░░▒█ ▒█▀▀▀ ▒█░░░ ▒█▀▀█ ▒█▀▀▀█ ▒█▀▄▀█ ▒█▀▀▀\n"
          "▒█▒█▒█ ▒█▀▀▀ ▒█░░░ ▒█░░░ ▒█░░▒█ ▒█▒█▒█ ▒█▀▀▀\n"
          "▒█▄▀▄█ ▒█▄▄▄ ▒█▄▄█ ▒█▄▄█ ▒█▄▄▄█ ▒█░░▒█ ▒█▄▄▄")
    print("\n       ＴＩＣ－ＴＡＣ－ＴＯＥ ＧＡＭＥ")
    print(f"{red_color}\n               Rules:{default_color}")
    print("     You are X, Computer is 𝖮.")
    print("     You can only chose a number from 1-9.")
    print("     Chose only one area with a number each turn.")
    print("     You cant chose an area already filled with 𝖮 or X.")
    print("     3 in row, line or diagonal wins the game")
    print(f"{green_color}\n    Would you like to play?{default_color} (y/n): ",
          end="")
    while True:
        choice = input()
        if choice == 'y' or choice == "Y":
            main()
        if choice == "n" or choice == "N":
            print("Thanks for playing! Goodbye.")
            exit()
        if choice != 'y' or choice != "n":
            print("Incorrect type. Please type y or n")


def play_again(player_name):
    while True:
        try:
            print(f"Would you like to play again {player_name}? y/n")
            choice = input()

            if choice == "y" or choice == "Y":
                clear_terminal()
                main()
                break
            elif choice == "n":
                print("Thanks for the game! Goodbye!")
                clear_terminal()
                exit()
            else:
                print(
                    f"{red_color}invalid input.{default_color}"
                    f" Type {green_color}y for yes{default_color},"
                    f" and{green_color} n for No{default_color}")
        except (ValueError, IndexError):
            print("Error, try agian!")


def choose_difficulty():
    """
    Let user to choose difficulty level Easy, Difficult and Hard,
    """
    while True:
        print("\nChoose difficult level !")
        print("\n1 Easy, 2 Difficult, 3 Hard ")
        choice = input("\n        Enter 1, 2 or 3: ")
        if choice == "1":
            clear_terminal()
            return computer_turn
        elif choice == "2":
            clear_terminal()
            return computer_turn_difficult
        elif choice == "3":
            clear_terminal()
            return computer_turn_lvl3
        else:
            print("invalid choice")


def main():
    """
    Runs the main function for the Tic-Tac-Toe game.
    """
    player_name = input("\n   Enter your name: ")
    clear_terminal()
    board = create_board()
    print_board(board)
    computer_move = choose_difficulty()
    print_board(board)
    print("\n         HAVE FUN AND GOOD LUCK !\n")
    while True:
        player_turn(board, player_name)
        clear_terminal()

        if check_winner(board, "X"):
            print_board(board)
            print(f"{green_color}\n"
                  "██╗░░░██╗██╗░█████╗░████████╗░█████╗░██████╗░██╗░░░██╗██╗\n"
                  "██║░░░██║██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚██╗░██╔╝██║\n"
                  "╚██╗░██╔╝██║██║░░╚═╝░░░██║░░░██║░░██║██████╔╝░╚████╔╝░██║\n"
                  "░╚████╔╝░██║██║░░██╗░░░██║░░░██║░░██║██╔══██╗░░╚██╔╝░░╚═╝\n"
                  "░░╚██╔╝░░██║╚█████╔╝░░░██║░░░╚█████╔╝██║░░██║░░░██║░░░██╗\n"
                  "░░░╚═╝░░░╚═╝░╚════╝░░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝\n"
                  f"{default_color}")
            play_again(player_name)
            break
        if check_tie(board):
            print_board(board)
            print("ITS A TIE!!")
            play_again(player_name)
            break

        computer_move(board)
        print_board(board)
        if check_tie(board):
            print_board(board)
            print("ITS A TIE!!")
            break
        if check_winner(board, "𝖮"):
            clear_terminal()
            print_board(board)
            print(f"{red_color}𝔾𝔸𝕄𝔼 𝕆𝕍𝔼ℝ ❕{default_color}")
            play_again(player_name)
            break


if __name__ == "__main__":
    while game_menu():
        main()
