# Find special characters in a file of words
# Usage: find_special.py <text.txt>

import sys
import os.path
import string

## Constants ##
class constants:
    UPPERS = list(string.ascii_uppercase)
    LOWERS = list(string.ascii_lowercase)
    NUMS   = [str(i) for i in range(0, 10)]
    VALID  = UPPERS + LOWERS + NUMS

## Functions ##

"""
.txt file -> stdout
Print list of speical characters found in .txt file to terminal
"""
def main():
    # Get file
    infile = get_file()
    if not infile:
        return
    
    specials = find_special(infile)
    print_chars(specials)
    return


"""
None -> String or False
Return the valid name of a .txt file from argument
        False if file is invalid
"""
def get_file():
    usage = "Usage: find-special.py <text.txt>"

    # Check valid usage
    if len(sys.argv) != 2:
        print(usage)
        return False
    
    input = sys.argv[1]

    # Check valid file type
    if not input.endswith(".txt"):
        print("Invalid file type")
        print(usage)
        return False
    
    # Check file exists
    if not os.path.exists(input):
        print("File does not exist")
        print(usage)
        return False
    
    # Check file is not empty
    if not os.path.getsize(input) > 0:
        print("File is empty")
        print(usage)
        return False
    
    return input


"""
String -> [listof Char]
Return list of characters not in [a-z, A-Z, 0-9] per word in file
ASSUME: word per line, no whitespace and no punctuation
"""
def find_special(file):
    specials = []

    with open(file, "r") as f:
        words = f.read().splitlines()
    for w in words:
        for c in w:
            if not c in specials and not c in constants.VALID:
                specials.append(c)

    return specials


"""
[listof Char] -> None
Print list of characters to terminal
"""
def print_chars(loc):
    for c in loc:
        print(c)
    return


# Run main
if __name__ == "__main__":
    main()
