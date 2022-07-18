# Replace special characters in a file
# Usage: replace_special.py <to_replace.txt> <output.txt>

from helpers import valid_usage, get_arg_file

## Constants ##
class constants:
    USAGE = "Usage: replace_special.py <to_replace.txt> <output.txt>"
    REPLACEMENTS = {
        "á": "a",
        "â": "a",
        "à": "a",
        "ç": "c",
        "é": "e",
        "è": "e",
        "í": "i",
        "ì": "i",
        "ï": "i",
        "ñ": "n",
        "ó": "o",
        "ò": "o",
        "ú": "u",
        "ü": "u",
    }


## Function ##

"""
.txt file -> .txt file
Create a new text file where all special characters are replaced by normal characters
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
    outfile = get_arg_file(2, constants.USAGE, ".txt", clear=True)
    if not outfile:
        return

    replace_special(infile, outfile)
    return


"""
String String -> .txt file
Create a new .txt file where all special characters from infile are replaced by normal characters
"""
def replace_special(infile, outfile):
    replacements = constants.REPLACEMENTS

    # Open outfile
    with open(infile, 'r') as inf:
        for line in inf:
            # Replace special characters
            for c in line:
                if c in replacements.keys():
                    line = line.replace(c, replacements[c])

            # Write to outfile
            with open(outfile, 'a') as outf:
                outf.write(line)
    return


# Run main
if __name__ == "__main__":
    main()
