# Find special characters in a file of words
# Usage: find_special.py <text.txt>

from helpers import valid_usage, get_arg_file
import string

## Constants ##
class constants:
    USAGE = "Usage: find-special.py <text.txt>"

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
    # Ensure valid command line usage
    if not valid_usage(2, constants.USAGE):
        return

    # Get file
    infile = get_arg_file(1, constants.USAGE, ".txt", mustexist=True, nonempty=True)
    if not infile:
        return
    
    specials = find_special(infile)
    print_chars(specials)
    return


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
