# Tic-Tac-Toe

Welcome to our Tic-Tac-Toe game! [Play here](https://bryar-2a68c072830e.herokuapp.com/)

It's a fun game, and you can play on your computer vs the computer.
This TIC-TAC-TOE is a Python terminal game.
Runs in the terminal and offers a quick and fun tic-tac-toe experience.
Players can enjoy a game against a computer opponent.
Two different difficulty settings.

![Tic-Tac-Toe Gameplay](/assets/images/amiviews_tictactoe.png)

## Introduction

This Python-based terminal game offers player vs computer.
Menu will be shown to read rules and how to play.
Computer has two difficulty levels, Easy and Hard.
Player can give his/her name from input field.
You can pick which one you want to play. 
In the game, you'll be "X" and the game will be "𝖮".
To win, you need to get three of your "X"s in a line before the game gets three "O"s in a line.


With this terminal Tic-Tac-Toe , you can enjoy the 3x3 grid. The colors and grid was done by using ANSI and ASCII and you can read more about it by clicking [here](https://www.gaijin.at/en/infos/ascii-ansi-character-table#:~:text=ASCII%20(American%20Standard%20Code%20for,the%20unchanged%20ASCII%20character%20set))


## How to Play

- **Start the Game:** Open your terminal and run the game. You'll be greeted with a menu.

- **Read the Rules:** Take a moment to look at the rules so you know how to play.

- **Enter Your Name:** When asked, type in your name. This is the name the game will use for you.

- **Pick a Difficulty:** Choose between 'Easy' and 'Hard' levels. If you're new, you might want to start with 'Easy'.

- **Make Your Move:** You'll play as 'X'. The game will ask you to pick a number to place your 'X' on the 3x3 grid.

- **Take Turns:** After your move, it's the computer's turn. They will place an '𝖮'. Keep taking turns.

- **Win the Game:** The first one to get three of their marks ('X' or '𝖮') in a row - up, down, across, or diagonally - wins the game!

- **Play Again:** After the game is over, you can choose to play again or exit the game.

## Features
- Menu
- Computer basic AI
- Player turn
- Type your name via user input
- Validation
- Checks for choices or moves already made
- Rturns result of game (winner, Tie or gameover)
- Gives player to play again or exit:
Game runs in loop till user exits


### Menu features
![](/assets/documents/Menu.png)
**Color Display:**
The game uses special ANSI color codes to make the text in your terminal colorful and visually appealing, enhancing your gaming experience.

**Easy to read:**
Designed with clarity in mind, the game's layout and text are spaced out for easy reading and navigation, ensuring a smooth game flow.

**Rules explained:**
The menu includes clear rules and instructions on how to play.

**Friendly Interface:**
From the welcoming message to the congratulatory remarks on winning, the game's interface is designed to be engaging and player-friendly.

**Start game or Exit:**
After each game, easily decide to play or exit. Just choose 'y' for yes to start the game, or 'n' for no to exit - the choice is yours!

**Computer turn**
- Play Easy:
This has random function which will be used to play easy.
The random funciton will look for cell with number and will occupy it with '𝖮'. 

- Play Hard:
The difficult level fucntion is for play hard.
Here it evaluates both rows and columns.
But it also checks for two occupied cell in row or in column.
Fills the third unoccupied cell with "𝖮" and blocks the third cell so that the players chance to win will decrease.

## Future Enhancements
- Make the Computer to check for diagnoal as well and occupie third cell in that diagonal row and even more advance like higher level
- Add multiboard aka Ultimate Tic Tac Toe. You can read more on wikipedia about it by clicking [here](https://en.wikipedia.org/wiki/Ultimate_tic-tac-toe)
- Add player vs player to menu so that two players can play together
- Add score and time
- Add to website with css style

## Testing
Game Initialization   
- Test case: Start the game and check if the main menu loads correctly
- Expected result: The main menu displays with options to read rules, start playing, or exit.

Display and Color Codes
- Test case: Observe the color and text display in the terminal.
- Expected result: ANSI color codes should correctly color the text. The layout should be clear and readable.

Player Name Input
- Test Case: Enter different names, including names longer than 15 characters and names with non-alphabetic characters.
- Expected Result: The game should accept names up to 15 alphabetic characters and prompt again for invalid inputs. In this case Anonymous is used as a name for test
![](/assets/documents/EnterName.png)

Game Board Creation
- Test Case: Start a new game and check the initial board layout.
- Expected Result: A 3x3 grid should be displayed, numbered from 1 to 9.
![](/assets/documents/Board.png)

Player Turn
- Test Case: During a player's turn, enter various inputs including valid and invalid cell numbers.
- Expected Result: The game should only accept numbers 1-9 for unoccupied cells. It should prompt again for invalid or occupied cells.

Computer Turn - Play Hard and Easy
- Test Case: Observe the computer's move.
- Action / Input: Watch the moves made by the computer opponent during a player's turn.
- Expected Result: The computer should place an 'O' in an unoccupied cell. In hard mode, it specifically looks for rows or columns where two cells are already occupied (either by 'X' or 'O') and attempts to fill the third cell with an 'O', thereby either trying to win or block the player's winning move.
![](/assets/documents/easy_vs_hard.png)

Winning Conditions
- Test Case: Align three 'X's horizontally, vertically, or diagonally.
- Expected Result: The game should correctly identify a win, end the game or play again choice given to the player.
![](/assets/documents/victory.png)

Tie Conditions
- Test Case: Fill all cells without a winning line.
- Expected Result: The game should recognize a tie and end the game. Here as well give option to the player if play again or exit by input or 'y' for play again or 'n' to exit 
![](/assets/documents/Tie.png)

Restart and Exit Options
- Test Case: Choose to restart or exit after a game.
- Expected Result: Selecting 'y' should start a new game, while 'n' should exit the program leaving terminal black.

Error Handling
- Test Case: Enter incorrect data types or out-of-range values during each step and stages. Especially the input stages and the outputs.
- Expected Result: Each step in the game should handle errors gracefully without crashing, providing appropriate feedback to the player.

Terminal Clearing
- Test Case: Check if the terminal clears correctly between games or during restarts.
- Expected Result: Previous game data should be cleared, showing only the current game information.

Game Exit
- Test Case: Exit the game from the main menu.
- Expected Result: The game should close without errors.
---
***Here is a table of the testing below:***

| Test Case # | Test Description                                | Action / Input                       | Expected Result                                    |
|-------------|-------------------------------------------------|--------------------------------------|----------------------------------------------------|
| 1           | Game Initialization                             | Start the game                       | Main menu loads with options                       |
| 2           | Display and Color Codes                         | Observe terminal                     | Correct colors and clear layout                    |
| 3           | Player Name Input                               | Enter various names                  | Accepts valid names, rejects invalid inputs       |
| 4           | Game Board Creation                             | Start new game                       | 3x3 grid displayed correctly                       |
| 5           | Player Turn                                     | Enter cell numbers (valid/invalid)   | Accepts 1-9 for unoccupied cells, prompts otherwise|
| 6           | Computer Turn                                   | Observe computer's move              | 'O' placed in an unoccupied cell                   |
| 7           | Difficulty Levels                               | Play on Easy and Hard                | Easy is random, Hard is strategic                  |
| 8           | Winning Conditions                              | Align three 'X's                     | Game identifies win and ends                       |
| 9           | Tie Conditions                                  | Fill all cells, no win               | Game recognizes tie and ends                       |
| 10          | Restart and Exit Options                        | Choose to restart or exit            | 'y' restarts, 'n' exits game                       |
| 11          | Error Handling                                  | Enter incorrect data                 | Handles errors without crashing                    |
| 12          | Terminal Clearing                               | Between games/restarts               | Clears previous game data                          |
| 13          | Game Exit                                       | Exit from main menu                  | Game closes without errors                         |



## Validator Testing
PEP8
- Results: All clear, no errors found
![](/assets/documents/pep8validator.png)

## Bugs
**Potential Bugs and Their Fixes**
- Input Validation Bug:

Description: Originally, the game did not properly handle non-numeric inputs or numbers outside the 1-9 range during a player's turn.
Fix: Implemented try-catch blocks to handle ValueError and IndexError. Now, if a player enters invalid data, the game prompts them to enter a valid cell number between 1 and 9.
- Computer Strategy Bug in Hard Mode:

Description: The computer's hard mode logic did not correctly identify opportunities to block the player's potential winning move.
Fix: Enhanced the algorithm in computer_turn_hard function to more accurately evaluate the board state, focusing on both offensive and defensive strategies.
- Color Display Bug in Certain Terminals:

Description: ANSI color codes were not displayed correctly in some terminal emulators, leading to unclear text and symbols.
Fix: Updated the color coding logic and tested across multiple terminal types to ensure compatibility and clear visibility.
- Tie Game Detection Bug:

Description: The game sometimes failed to recognize a tie situation, causing it to prompt for further moves even when no cells were left.
Fix: Refined the check_tie function to correctly identify when all cells are occupied without any player winning, declaring a tie.
- Player Name Input Bug:

Description: Players were able to enter names with non-alphabetic characters, contrary to the game's intended design.
Fix: Updated the create_player_name function to strictly validate that only alphabetic characters are used in player names.

### Potential Bugs
- Computer Strategy Optimization:

In computer_turn_hard, the computer's strategy might not be optimal. It checks for immediate winning or blocking opportunities but may not plan moves ahead, which could be improved for a more challenging AI.

- Game Replay Flow:

The play_again function could potentially have issues with the game state reset, ensuring a completely new game setup for each replay. e.g Player need to always type name again, but this could also be in the
[Future Enhancements](#future-enhancements).

## Logic path
- Game Architecture Diagram

To provide a clearer picture of the game's code structure and logic, we have created a comprehensive flowchart using Lucidchart. This diagram breaks down the execution flow of `run.py`, illustrating how the game progresses from start to finish and how the different functions interact with each other for an easier guide to build the game and its fucntions.

![View the full diagram here](/assets/documents/lucichart.png)


## Deployment

- Steps
1. Fork or clone this repository
2. Create new app in Heroku
3. Set the buildbacks to Python on top and NodeJS under
4. Next link the Heroku app to the repository inside Heroku
5. Click on Deploy

## Development Tools and Techniques
1. Python
2. Github
3. Heroku
4. Lucidchart

## Screenshots
[My GitHub Documents](https://github.com/Bryaro/project-3/tree/main/assets/documents)


## Credits
- Font generator
- wikipedia
- Font generator [FSYMBOLS ](https://fsymbols.com/)
- Readme formats [Basic writing and formatting syntax](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax#relative-links)
- Clears the terminal
    Original code from [here](    http://www.coding4you.at/inf_tag/beginners_python_cheat_sheet.pdf)
    Recommended to me by Goran Sigeskog
    [His GitHub](https://github.com/gorsig)

    [Back to Top](#tic-tac-toe)