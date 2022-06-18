# A terminal Sudoku game

# === Data Definitions ===


# Value is [1, 9]
# Interp. a valid Sudoku move value

# List of valid values
VALUE = [i for i in range(1, 10)]


# Board is [Value || False][Value || False]   where each list is 9 elements long
# for a total of 81 elements.
# interp. A Sudoku Board

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
    
    # Move -> Boolean
    # Return true if Move is valid
    # ('B', 7, 4) should return True
    # ('J', 9, 0) should return False
    def isvalid(self):
        if (self.indexl in L_INDEX and self.indexu in U_INDEX and self.value in VALUE):
            return True
        else:
            return False


# == Funcitons ==


def main():

    # Constants ==
    prompt = "数独> "

    # Print header
    print("Terminal Sudoku")
    print("P to play, ^C to exit.")
    print()

    # Start game once user inputs p
    while True:
        if (input(prompt).upper() == 'P'):
            print()
            break

    while True:

        # Get user input for move
        move = input(prompt)

        # Store move as a Move
        move = Move(move[0], move[1], move[3])

        # Check for move validity
        if (move.isvalid()):
            print("Valid move.")
        else:
            print("Invalid move.")


# Board -> Terminal Output
# for printing a Board to terminal
# printboard(B1) should output:
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

def printboard(b):
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
            if (b[i][j] == False):
                print(". ", end="")
            # Otherwise print number
            else:
                print(f'{b[i][j]} ', end="")
            
            # Print divider between squares
            if (j in [2, 5, 8]):
                print("| ", end="")
        
        # Print newline
        print()
    
    # Print last divider
    printdivider()



# Run main
if __name__ == '__main__':
    main()
