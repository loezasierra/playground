# Filter words of certain length
# Usage: of_length.py <number> <to_filter.txt> <outfile.txt>

import sys
from helpers import valid_usage, get_arg_file

## Constants ##
class constants:
    USAGE = "Usage: of_length.py <number> <to_filter.txt> <outfile.txt>"

"""
Int .txt file -> .txt file
Create a new file with words of given length from given file
"""
def main():
    # Ensure valid command line usage
    if not valid_usage(4, constants.USAGE):
        return

    # Get valid filter length
    length = valid_length()
    if not length:
        return
    
    # Get valid infile
    infile = get_arg_file(2, constants.USAGE, ".txt", mustexist=True, nonempty=True)
    if not infile:
        return
    
    # Get valid outfile
    outfile = get_arg_file(3, constants.USAGE, ".txt", clear=True)
    if not outfile:
        return
    
    filter_words(length, infile, outfile)
    return


"""
None -> Int or False
Return length if given a valid non-zero integer at command line
        Return False otherwise
"""
def valid_length():
    l = sys.argv[1]

    try:
        l = int(l)
        if l < 0:
            print("Length must be a non-zero integer")
            print(constants.USAGE)
            return False
    except:
        print("Length must be a non-zero integer")
        print(constants.USAGE)
        return False
    
    return l


"""
Int String String -> .txt file
Create a new file with only words of given length
"""
def filter_words(length, infile, outfile):
    with open(infile, 'r') as f:
        words = f.read().splitlines()
    
    words = filter(lambda w: len(w) == length, words)
    
    with open(outfile, 'w') as f:
        for w in words:
            f.write(w)
            f.write('\n')
    return


# Run main
if __name__ == '__main__':
    main()
