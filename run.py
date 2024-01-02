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
    Handles a player's turn in Tic-Tac-Toe.
    Prompts the player to select a cell by number (1-9).
    Checks for valid and unoccupied cell selection.
    Repeats prompt for invalid choices.
    Args:
        board (list): Current Tic-Tac-Toe board state.
        player_name (str): Player's name.
    Updates the board with the player's move. No return value.
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
    If the random selected cell is unoccupied, it marks the cell with '𝖮'.
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
    Create a medium difficulty level (Level 2) for the computer's turn.
    This function checks each row of the board. If it finds a row with
    two cells already occupied by 'X' (the player's mark), it occupies
    the remaining unoccupied cell with '𝖮' (the computer's mark) to block
    the player's potential win. If no such opportunity exists, it defaults
    to making a random move.
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
    Create a hard difficulty level (Level 3) for the computer's turn.
    This function checks each row of the board. If it finds a row with
    either two cells occupied by exactly two 'X' or two by '𝖮', it occupies the
    remaining unoccupied cell in that row with '𝖮'.
    This serves two purposes: blocking
    the player's potential win (if two 'X's are found) and creating a winning
    line for the computer (if two '𝖮's are found). If no such opportunity
    exists, it defaults to making a random move.
    """
    for row in board:
        if row.count("X") == 2 or row.count("𝖮") == 2:
            for i in range(3):
                if isinstance(row[i], int):
                    row[i] = "𝖮"
                    return
    computer_turn(board)


def computer_turn_lvl4(board):
    """
    Create a hard difficulty level (Level 4) for the computer's turn.
    Here it evaluates both rows and columns.
    Checks for two occupied cell in row or in column.
    Fills the third unoccupied cell with "𝖮"
    """
    for col in range(3):
        column = [board[row][col] for row in range(3)]

        if column.count("X") == 2 or column.count("𝖮") == 2:
            for row in range(3):
                if isinstance(board[row][col], int):
                    board[row][col] = "𝖮"
                    return
    for row in board:
        if row.count("X") == 2 or row.count("𝖮") == 2:
            for i in range(3):
                if isinstance(row[i], int):
                    row[i] = "𝖮"
                    return

    computer_turn(board)


def check_winner(board, player):
    """
    Checks for a winning condition for the specified player on the board.
    Args:
        board (list): The 3x3 Tic-Tac-Toe board state.
        player (str): The player's mark ('X' or '𝖮').
    Returns:
        bool: True if the player has won (three marks in a row, column,
        or diagonal), False otherwise.
    """
    # check if winning in each row
    for i in range(3):
        if (board[i][0] == player and
                board[i][1] == player and
                board[i][2] == player):
            return True
        if (board[0][i] == player and
                board[1][i] == player and
                board[2][i] == player):
            return True
    # checks if diagonal winning from top-left to bottom right
    if (board[0][0] == player and
            board[1][1] == player and
            board[2][2] == player):
        return True
    # checks if diagonal winning from top right to bottom left
    if (board[2][0] == player and
            board[1][1] == player and
            board[0][2] == player):
        return True
    return False


def check_tie(board):
    """
    Evaluates if the game is a tie.
    A tie is when all board cells are filled without any player winning.
    The function checks each cell for a tie condition.
    Args:
        board (list of lists): 3x3 Tic-Tac-Toe board.
    Returns:
        bool: True for a tie, False otherwise.
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
    Displays the main menu of the Tic-Tac-Toe game.
    This function presents the game's main menu to the user, showing
    game rules and the option to start playing. It handles user input
    to either start the game or exit. If the user chooses to play, it
    calls the main game function.
    No arguments or return values. User interaction is handled through
    input prompts and print statements.
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
    """
    Prompts the player to play another game or exit.
    After a game concludes, this function asks the player if they want to
    play another round. Based on the player's response, it either restarts
    the game or terminates the program.
    Args:
        player_name (str): The name of the player.
    No return value. Directly calls main() to restart or exits the program.
    """
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
    Allows the player to select a difficulty level for the game.
    Presents options for different difficulty levels and sets the computer's
    playing strategy based on the player's choice.
    Returns:
        function: Computer turn function based on difficulty level.
    """
    while True:
        print("\nChoose difficult level !")
        print("\n1 Easy, 2 Difficult, 3 Hard, 4 Advanced ")
        choice = input("\n        Enter 1, 2, 3 or 4: ")
        if choice == "1":
            clear_terminal()
            return computer_turn
        elif choice == "2":
            clear_terminal()
            return computer_turn_difficult
        elif choice == "3":
            clear_terminal()
            return computer_turn_lvl3
        elif choice == "4":
            clear_terminal()
            return computer_turn_lvl4
        else:
            print("invalid choice")


def main():
    """
    Runs the main game loop of Tic-Tac-Toe.
    Handles the overall game process including player input.
    displaying the board. Alternating turns between player and computer.
    Runs till the game ends.
    No arguments or return values. Calls other functions to manage game flow.
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
