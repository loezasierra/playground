# A terminal Sudoku game

# === Data Definitions ===

# Value is [1, 9]

# Board is [Value || False][Value || False]   where each list is 9 elements long
# for a total of 81 elements.
# interp. A Sudoku Board

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

