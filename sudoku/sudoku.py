# A terminal Sudoku game

# === Data Definitions ===


# Value is [1, 9]
# Interp. a valid Sudoku move value

# List of valid values
VALUE = [i for i in range(1, 10)]


# BOARD is Board([Value || False][Value || False])   where each list is 9 elements long
# for a total of 81 elements.
# interp. A Sudoku Board
class Board:
    def __init__(self, b):
        self.board = b
    
    # Board -> Terminal Output
    # for printing a Board to terminal
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

# For easy example Board making
B = False

# A blank Sudoku Board
B0 = Board([
    [B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B],
    [B, B, B, B, B, B, B, B, B]
])

# An easy Sudoku Board
B1 = Board([
    [B, 8, B, 7, B, 1, B, 3, B],
    [4, B, 9, B, B, B, B, B, B],
    [B, 5, B, B, 6, B, 4, 1, 8],
    [7, B, B, B, B, 9, B, B, B],
    [8, B, B, 6, 1, B, 5, B, B],
    [B, 3, 5, B, B, B, B, 2, 9],
    [B, 6, B, 4, B, 7, B, 9, B],
    [1, B, B, B, B, 8, B, B, 4],
    [B, B, B, B, 5, B, B, 7, B]
])


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
    # Return true if input is 'P'
    # "P" should return True
    # "p" should return True
    # Any other single char should return False
    # Any string longer than 1 should return False
    def play(self):
        return (self.input.upper() == 'P')
    
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
    print("'p' to play, 'q' to exit.")
    print()

    # Start game if user inputs 'p', quit if 'q'
    while True:
        user = UserInput(input(prompt))

        if user.play():
            print()
            break
        if user.quit():
            return

    while True:

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
        board.fill(move)



# Run main
if __name__ == '__main__':
    main()
