from board import Board
from enum import auto
from textwrap import dedent
import sys

class InputStatus:
    QUIT = auto()
    OPEN = auto()
    INVALID = auto()
    HELP = auto()
    PRINT = auto()
    SOLUTION = auto()

BOARD_SIZE = 3
MINE_COUNT = 2

def validate_input(command):
    if (command == 'q' or command == 'quit'):
        return InputStatus.QUIT
    if (command == 'h' or command == 'help'):
        return InputStatus.HELP
    if (command == 'p' or command == 'print'):
        return InputStatus.PRINT
    # cheat code
    if (command == 'polo' or command == 'marco' or command == 'marco polo'):
        return InputStatus.SOLUTION
    fields = command.split()
    if len(fields) == 2 and fields[0].isdigit() and fields[1].isdigit():
        row = int(fields[0])
        col = int(fields[1])
        if row <= 0 or row > BOARD_SIZE or col <= 0 or col > BOARD_SIZE:
            return InputStatus.INVALID
        return InputStatus.OPEN
    return InputStatus.INVALID

game_board = Board(BOARD_SIZE, MINE_COUNT)
game_board.display_board()
game_board.show_solution()

is_game_solved = game_board.is_solved()
while True and is_game_solved is False:
    try:
        command = input("Open row and column (h for help):")
        match validate_input(command):
            case InputStatus.QUIT:
                print('Exiting the game')
                sys.exit()
            case InputStatus.OPEN:
                fields = command.split()
                row = int(fields[0]) - 1
                col = int(fields[1]) - 1
                game_board.open_tile(row, col)
                game_board.display_board()
            case InputStatus.INVALID:
                print('Invalid input')
                continue
            case InputStatus.PRINT:
                game_board.display_board()
                continue
            case InputStatus.SOLUTION:
                game_board.show_solution()
                continue
            case InputStatus.HELP:
                message = dedent(f'''
                      Help:
                      Enter row and column separated by space
                      with valid values from 1 to {BOARD_SIZE}.
                      Ex: {BOARD_SIZE} 1
                      Enter 'p' or 'print' to print board.
                      Enter 'q' or 'quit' to quit.
                      ''')
                print(message)
                continue

        is_game_solved = game_board.is_solved()
        print(f'Board is solved: {is_game_solved}')
    except Exception as e:
        print(e)
        sys.exit()
