# Helpers for Terminal Sudoku


# === Constans ===

# File paths
easy_path   = "./puzzles/simple.csv"
medium_path = "./puzzles/easy.csv"
hard_path   = "./puzzles/intermediate.csv"
expert_path = "./puzzles/expert.csv"


# === Data Definitions ===


# Value is [1, 9]
# Interp. a valid Sudoku value

# List of valid values
VALUE = [i for i in range(1, 10)]


# SudokuChar is 'Value'|'.'
# Interp. a valid Sudoku Character in a Sudoku String
#        '.' is a blank

SC0 = '.'
SC1 = '7'

# SudokuString is String of length 81 where each character is a SudokuChar
# Interp. a valid Sudoku String

SS0 = ".8.7.1.3.4.9.......5..6.4187....9...8..61.5...35....29.6.4.7.9.1....8..4....5..7."
SS1 = "286741935419385762357962418741529386892613547635874129568437291173298654924156873"


# Board is [Value || False][Value || False]   where each list is 9 elements long
# for a total of 81 elements.
# interp. A valid Sudoku Board

# For easy example board making
B = False

# A blank Sudoku Board
B0 = [
    [B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B]
]

# An easy Sudoku Board
# Source: https://image.shutterstock.com/image-vector/vector-sudoku-answer-164-puzzle-260nw-1168048867.jpg
B1 = [
    [B, 8, B, 7, B, 1, B, 3, B],
    [4, B, 9, B, B, B, B, B, B],
    [B, 5, B, B, 6, B, 4, 1, 8],
    [7, B, B, B, B, 9, B, B, B],
    [8, B, B, 6, 1, B, 5, B, B],
    [B, 3, 5, B, B, B, B, 2, 9],
    [B, 6, B, 4, B, 7, B, 9, B],
    [1, B, B, B, B, 8, B, B, 4],
    [B, B, B, B, 5, B, B, 7, B]
]

B1S = [
    [2, 8, 6, 7, 4, 1, 9, 3, 5],
    [4, 1, 9, 3, 8, 5, 7, 6, 2],
    [3, 5, 7, 9, 6, 2, 4, 1, 8],
    [7, 4, 1, 5, 2, 9, 3, 8, 6],
    [8, 9, 2, 6, 1, 3, 5, 4, 7],
    [6, 3, 5, 8, 7, 4, 1, 2, 9],
    [5, 6, 8, 4, 3, 7, 2, 9, 1],
    [1, 7, 3, 2, 9, 8, 6, 5, 4],
    [9, 2, 4, 1, 5, 6, 8, 7, 3]
]


class Sudoku:
    # Sudoku is Sudoku(Board, Board)
    # interp. A Sudoku game where Solution is the solution to Game
    def __init__(self, g, s):

        # Sudoku Board to play
        self.game = g

        # Solution
        self.solution = s

S1 = Sudoku(B1, B1S)


# Difficulty is one of:
# - 'easy'
# - 'medium'
# - 'hard'
# - 'expert'
# interp. Difficulty of a Sudoku Game
#         'easy'   Contains only Singles
#         'medium' Contains Hidden Singles
#         'hard'   Contains Naked Pairs, Hidden Pairs, Pointing Pairs/Triples and/or Box/Line Intersections
#         'expert' Contains Guessues and/or Backtracks



# === Functions ===

# Difficulty -> Sudoku
# return a random Sudoku of given difficulty from appropriate file
# getsudoku('easy') should return random Sudoku from easy_path
def getsudoku(dif):
    return S1
