import random
import os

# Define ANSI color codes for terminal text coloring
green_color = "\033[92m"
red_color = "\033[91m"
default_color = "\033[0m"

# Define indentation constants for formatting output
indent = "\t\t\t"
board_indent = "\t\t\t\t\t"


def create_board():
    # Initialize an empty list to represent the Tic-Tac-Toe board
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

    for i in range(3):  # Loop to create each row of the board
        row = []
        for j in range(3):
            row.append(cell_number)
            cell_number += 1
        board.append(row)  # Add the completed row to the board

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
    row_counter = 0
    print("\n\n\n")
    for row in board:
        print(board_indent + " ┃ ".join(str(cell) for cell in row))
        row_counter += 1  # Increment the row counter after printing each row
        if row_counter < 3:  # Only print separator if it's not the last row
            print(board_indent + "━" + "━╋━" + "━" + "━╋━━")


def create_player_name():
    """
    Prompts the user to enter a valid player name.
    Validates that the name is a string and no longer than 15 characters.
    """
    while True:
        player_name = input(indent + "\n\n     Enter your name "
                            "(up to 15 characters, no numbers): ")
        if player_name.isalpha() and len(player_name) <= 15:
            return player_name
        else:
            print("     Invalid name. "
                  "Please enter your name with Maximum of 15 characters.")


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
                f"\n{indent}{player_name}'s turn."
                " Enter a number 1-9:\n"))
            row = (turn - 1) // 3
            col = (turn - 1) % 3

        # Check if the selected cell is unoccupied
            if board[row][col] == turn:
                board[row][col] = "X"  # Mark cell with 'X' for player's move
                break
            else:
                print("\n                cell already taken. Try again\n")
        except (ValueError, IndexError):
            # Handle invalid input or out-of-range selections
            print("                You typed invalid data, "
                  "Type only a number bewteen 1-9\n")


def computer_turn(board):
    """
    Create computer turn
    Randomly selects a cell on the board for the computer's turn.
    If the random selected cell is unoccupied, it marks the cell with '𝖮'.
    """
    while True:
        turn = random.randint(1, 9)
        row = (turn - 1) // 3
        col = (turn - 1) % 3
        if board[row][col] == turn:
            board[row][col] = "𝖮"
            break


def computer_turn_hard(board):
    """
    Create a hard difficulty level for the computer's turn.
    Here it evaluates both rows and columns.
    Checks for two occupied cell in row or in column.
    Fills the third unoccupied cell with "𝖮"
    """
    # Check each column for a potential winning or blocking opportunity
    for col in range(3):
        column = [board[row][col] for row in range(3)]

        if column.count("X") == 2 or column.count("𝖮") == 2:
            for row in range(3):
                if isinstance(board[row][col], int):
                    board[row][col] = "𝖮"
                    return

    # Check each row for a potential winning or blocking opportunity
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
            # Increment count for each cell occupied by 'X' or '𝖮'
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
    print("\n\n" + indent + f"{green_color}" "█░█░█ █▀▀ █░░ █▀▀ █▀█ █▀▄▀█ █▀▀")
    print(indent + f"{green_color}" "▀▄▀▄▀ ██▄ █▄▄ █▄▄ █▄█ █░▀░█ ██▄\n")
    print(indent + f"{green_color}""        TIC-TAC-TOE GAME")
    print(f"{red_color}\n     Rules:{default_color}\n")
    print("     - You are X, Computer is 𝖮.")
    print("     - You can only chose a number from 1-9.")
    print("     - Chose only one area with a number each turn.")
    print("     - You cant chose an area already filled with 𝖮 or X.")
    print("     - 3 in row, line or diagonal wins the game")
    print(f"{green_color}\n     Would you like to play?{default_color}"
          "(y/n): ", end="")
    while True:
        choice = input()
        if choice == 'y' or choice == "Y":
            main()
        if choice == "n" or choice == "N":
            print("     Thanks for playing! Goodbye.")
            exit()
        if choice != 'y' or choice != "n":
            print("     Incorrect type. Please type y or n")


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
            print(f"\n        Would you like to play again {player_name}? y/n")
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
        clear_terminal()
        print("\n           Choose the difficulty level!")
        print("\n           - 1 for Easy")
        print("\n           - 2 for Hard")
        choice = input(indent + "\n           Enter 1 or 2: ")
        if choice == "1":
            clear_terminal()
            return computer_turn
        elif choice == "2":
            clear_terminal()
            return computer_turn_hard
        else:
            print("\n           invalid choice")


def main():
    """
    Runs the main game loop of Tic-Tac-Toe.
    Handles the overall game process including player input.
    displaying the board. Alternating turns between player and computer.
    Runs till the game ends.
    No arguments or return values. Calls other functions to manage game flow.
    """
    player_name = create_player_name()
    clear_terminal()
    board = create_board()
    print_board(board)
    computer_move = choose_difficulty()
    print_board(board)
    print(f"\n{indent}WELCOME {player_name} !")
    print(indent + "HAVE FUN AND GOOD LUCK !")
    while True:
        player_turn(board, player_name)
        clear_terminal()

        if check_winner(board, "X"):
            print("\n\n\n")
            print(f"{green_color}"
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
            print("")
            print(indent + "ITS A TIE!!")
            play_again(player_name)
            break

        computer_move(board)
        print_board(board)
        if check_winner(board, "𝖮"):
            clear_terminal()
            print_board(board)
            print("")
            print(indent + f"{red_color}𝔾𝔸𝕄𝔼 𝕆𝕍𝔼ℝ❕{default_color}")
            play_again(player_name)
            break


if __name__ == "__main__":
    while game_menu():
        main()
