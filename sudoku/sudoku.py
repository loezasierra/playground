# A terminal Sudoku game

# === Constants ===

# valid difficulties
difficulty = {
    0 : "easy",
    1 : "medium",
    2 : "hard",
    3 : "expert"
}

# === Data Definitions ===


# Value is [1, 9]
# Interp. a valid Sudoku move value

# List of valid values
VALUE = [i for i in range(1, 10)]


# GameBoard is [Value || False][Value || False]   where each list is 9 elements long
# for a total of 81 elements.
# interp. A playable Sudoku Board
#         False is Empty Square

# For easy example Board making
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


# SolutionBoard is [Value][Value]   where each list is 9 elements long
# for a total of 81 elements
# interp. the solution to a GameBoard

# Solution for B1
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


class Board:
    # Board is Board(GameBoard, SolutionBoard)
    # interp. A playable Sudoku Board with its solution

    def __init__(self, b, s):
        # GameBoard
        self.board = b

        # SolutionBoard
        self.solution = s

        # FILLABLE is Fillable([Bool][Bool])   where each list is 9 elements long
        # interp. The fillable positions by user on the board
        #         True means user is able to fill element on Board
        #         False means user is not able to fill square (part of the puzzle)
        # B1.fillable() should output B1F
        # Example at end of object definition
        self.fillable = [[j == False for j in i] for i in self.board]

    # Board -> Terminal Output
    # for printing a GameBoard to terminal
    # B1.printboard() should output:
    """
        0 1 2   3 4 5   6 7 8
    -------------------------
    A | . 8 . | 7 . 1 | . 3 . |
    B | 4 . 9 | . . . | . . . |
    C | . 5 . | . 6 . | 4 1 8 |
    -------------------------
    D | 7 . . | . . 9 | . . . |
    E | 8 . . | 6 1 . | 5 . . |
    F | . 3 5 | . . . | . 2 9 |
    -------------------------
    G | . 6 . | 4 . 7 | . 9 . |
    H | 1 . . | . . 8 | . . 4 |
    I | . 2 . | . 5 . | . 7 . |
    -------------------------
    """

    def printboard(self):
        # Print number header
        print("    0 1 2   3 4 5   6 7 8")

        # For printing divider
        def printdivider():
            # Print starting indent
            print("  ", end="")

            for i in range(24):
                print("-", end="")

            # Print last - with newline
            print("-")

        # Starting left side indeces at 'A'
        index = 'A'

        for i in range(9):
            # Print dividers between rows
            if (i % 3 == 0):
                printdivider()
            
            # Print left side index
            print(index + " | ", end="")
            
            # Advance index by 1 character for next iteration
            index = chr(ord(index) + 1)

            for j in range(9):
                # Print . if false
                if (self.board[i][j] == False):
                    print(". ", end="")
                # Otherwise print number
                else:
                    print(f'{self.board[i][j]} ', end="")
                
                # Print divider between squares
                if (j in [2, 5, 8]):
                    print("| ", end="")
            
            # Print newline
            print()
        
        # Print last divider
        printdivider()
    

    # Board Move -> Bool
    # fill board with the given move
    #   return True if fill was successfull
    #   return False if fill was unseccessfull (as in trying to fill an unfillable square)
    # B1 Move('A', 0, 5) should put a '5' at the top right of B1 and return True
    # B1 Move('I', 8, 7) should put a '7' at the bottom left of B1 and return True
    # B1 move('A', 1, 7) should return False
    def fill(self, move):
        if (self.fillable[L_INDEX.index(move.indexl)][move.indexu]):
            self.board[L_INDEX.index(move.indexl)][move.indexu] = move.value
            return True
        else:
            return False

# For easy example Fillable board making
T = True
F = False

# Fillable positions for B1
B1F = [
    [T, F, T, F, T, F, T, F, T],
    [F, T, F, T, T, T, T, T, T],
    [T, F, T, T, F, T, F, F, F],
    [F, T, T, T, T, F, T, T, T],
    [F, T, T, F, F, T, F, T, T],
    [T, F, F, T, T, T, T, F, F],
    [T, F, T, F, T, F, T, F, T],
    [F, T, T, T, T, F, T, T, F],
    [T, T, T, T, F, T, T, F, T]
]

BOARD1 = Board(B1, B1S)


# L_INDEX is ['A', 'I']
# interp. An index on the left side of the board

# List of left side indices
L_INDEX = [chr(i) for i in range(ord('A'), ord('J'))]


# U_INDEX is [0, 8]
# interp. An index on the top of the board

# List of top indices
U_INDEX = [i for i in range(9)]


# MOVE is Move(L_INDEX, U_INDEX, VALUE)
# interp. a Sudoku move
#         L_INDEX is the row of the move
#         U_INDEX is the column of the move
#         VALUE   is the value to put in row, column
#         isvalid returns True if Move is valid
class Move:
    def __init__(self, indexl, indexu, val):
        self.indexl = indexl.upper()
        self.indexu = int(indexu)
        self.value = int(val)

M0 = Move('A', 0, 5) # A move to place 5 at top left of Board
M1 = Move('I', 8, 7) # A move to place 7 at bottom right of Board


# USER_INPUT is UserInput(String)
# interp. Input from the user at terminal
#         play returns True if input is 'P'
#         quit returns True if input is 'Q'
#         ismove returns True if input is MOVE_INPUT
class UserInput:
    def __init__(self, input):
        self.input = input
    
    # USER_INPUT -> Boolean
    # Return true if input is a valid difficulty
    # "0" should return True
    # "3" should return True
    # "4" should return False
    # Any other single char should return False
    # Any string longer than 1 should return False
    def play(self):
        valid = [str(d) for d in difficulty.keys()]
        return (self.input in valid)
    
    # USER_INPUT -> Boolean
    # Return true if input is 'Q"
    # "Q" should return True
    # "q" should return True
    # Any other single char should return False
    # Any string longer than 1 should return False
    def quit(self):
        return (self.input.upper() == 'Q')
    
    # USER_INPUT -> Boolean
    # Return true if input is MOVE_INPUT
    # "B2 7" should return True
    # "C9 8" should return False
    # "D609" should return False
    def ismove(self):
        # Return false if input length not 4
        if (len(self.input) != 4):
            return False

        # Check for valid characters
        try:
            indexl = self.input[0].upper()
            indexu = int(self.input[1])
            space = self.input[2]
            value = int(self.input[3])
        except:
            return False

        return (indexl in L_INDEX and indexu in U_INDEX and space == ' ' and value in VALUE)


# MOVE_INPUT is String of size 4
# interp. a move input from user at terminal
#         i[0] is L_INDEX
#         i[1] is U_INDEX
#         i[2] is " ", a space
#         i[3] is VALUE

# Valid MOVE_INPUT
VMI1 = "B2 7"
VMI2 = "D6 9"


# == Funcitons ==


def main():

    # Constants ==
    prompt = "数独> "

    # Print header
    print("Terminal Sudoku")
    print()
    print("Choose a difficulty:")
    for d in difficulty:
        print(f"  '{d}' for {difficulty[d]}")
    print("'q' to exit.")
    print()

    # Start game if user inputs a difficulty, quit if 'q'
    while True:
        user = UserInput(input(prompt))

        if user.play():
            print()
            break
        if user.quit():
            return
    
    # Store game board
    board = BOARD1

    while True:

        # Print game board
        board.printboard()

        # Print correct move formatting
        print('Valid move is "RowColumn Value"')
        print('example: "B2 7"')

        # Get user input
        user = UserInput(input(prompt))

        # Quit if user inputs 'q'
        if user.quit():
            return

        # Validate user input as valid move input
        if user.ismove():
            # Store input as a Move
            move = Move(user.input[0], user.input[1], user.input[3])
        else:
            # Let user know of invalid input
            print("Invalid input")
            print()
            continue

        # Fill game board with move
        if (not board.fill(move)):
            # Let user know if trying to fill an unfillable square
            print("Can't fill that square")
            print()



# Run main
if __name__ == '__main__':
    main()
