# Sort a file of strings
# Usage: sort.py <to_sort.txt> <outfile.txt>

from helpers import valid_usage, get_arg_file

## Constatns ##
class constants:
    USAGE =  "Usage: sort.py <to_sort.txt> <outfile.txt>"

"""
.txt file -> .txt file
Create a new text file where all lines of strings from given file are sorted alphabetically
"""
def main():
    # Ensure valid command line usage
    if not valid_usage(3, constants.USAGE):
        return
    
    # Get valid infile
    infile = get_arg_file(1, constants.USAGE, ".txt", mustexist=True, nonempty=True)
    if not infile:
        return
    
    # Get valid outfile
    outfile = get_arg_file(2, constants.USAGE, ".txt")
    if not outfile:
        return
    
    sort_lines(infile, outfile)    
    return


"""
String String -> .txt file
Create a new .txt file where all lines from infile are sorted alphabetically
"""
def sort_lines(infile, outfile):
    return


# Run main
if __name__ == "__main__":
    main()
