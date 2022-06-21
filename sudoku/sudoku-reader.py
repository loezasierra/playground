# A CSV Sudoku File Reader
# Takes CSV generated from https://qqwing.com/generate.html as command line argument
# and and separates into CSV files based on difficulty
# Usage: python sudoku-reader.py qqwing-boards.csv

import sys
import csv

# Read command line argument
file = sys.argv[1]

# Read csv file of sudoku boards
with open(file, newline='') as infile:
    # Read as dictionary
    reader = csv.DictReader(infile)

    # Per board
    for board in reader:
        # Read the board's difficulty
        difficulty = board['Difficulty'].lower()

        # Open the corresponding csv file
        with open(difficulty + ".csv", 'a', newline='') as outfile:

            # Write as dictionary
            writer = csv.DictWriter(outfile, fieldnames=['Puzzle', 'Solution'])

            # Write header if no file exists yet
            if outfile.tell() == 0:
                writer.writeheader()

            # Write the puzzle with solution to file
            writer.writerow({'Puzzle': board['Puzzle'], 'Solution': board['Solution']})
