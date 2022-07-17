# Replace special characters in a file
# Usage: replace_special.py <to_replace.txt> <output.txt>

import sys
import os.path

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
    if not validate():
        return

    # Get valid infile
    infile = get_infile()
    if not infile:
        return
    
    # Get valid outfile
    outfile = get_outfile()
    if not outfile:
        return

    replace_special(infile, outfile)
    return


"""
None -> Bool
Return true if given 2 arguments (infile and outfile)
"""
def validate():
    if len(sys.argv) != 3:
        print(constants.USAGE)
        return False        
    return True


"""
None -> String or False
Return the name of a valid and existing .txt file from first command line argument
        False if file is invalid
"""
def get_infile():
    infile = sys.argv[1]

    # Check valid file type
    if not infile.endswith(".txt"):
        print("Invalid file type")
        print(constants.USAGE)
        return False
    
    # Check file exists
    if not os.path.exists(infile):
        print("File does not exist")
        print(constants.USAGE)
        return False
    
    # Check file is not empty
    if not os.path.getsize(infile) > 0:
        print("File is empty")
        print(constants.USAGE)
        return False

    return infile


"""
None -> String or False
Return the name of a valid .txt file from second command line argument
        False if file name is invalid
"""
def get_outfile():
    outfile = sys.argv[2]

    # Check valid file type
    if not outfile.endswith(".txt"):
        print("Invalid file type")
        print(constants.USAGE)
        return False
    
    # Clear file if it already exists
    if os.path.exists(outfile):
        open(outfile, 'w').close()
    
    return outfile


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
