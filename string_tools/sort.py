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
    with open(infile, 'r') as f:
        words = f.read().splitlines()
    
    words = sort_words(words)
    
    with open(outfile, 'w') as f:
        for w in words:
            f.write(w)
            f.write('\n')
    return


"""
[listof String] -> [listof String]
Return the given list of words sorted alphabetically using merge sort
ASSUME: List contains at least one word
"""
def sort_words(words):
    # Base case
    if len(words) == 1:
        return words
    else:
        # Sort separate lists
        middle = round(len(words) / 2)
        left = sort_words(words[0:middle])
        right = sort_words(words[middle:len(words)])

        merged = []

        # For traversing left and right
        l = 0
        r = 0

        while l < len(left) or r < len(right):
            # If left empty, add rest of right to merged
            if l >= len(left):
                merged = merged + right[r:len(right)]
                break
            # If right empty, add rest of left to merged
            elif r >= len(right):
                merged = merged + left[l:len(left)]
                break
            # Merge next words alphabetically
            elif left[l] < right[r]:
                merged.append(left[l])
                l += 1
            else:
                merged.append(right[r])
                r += 1

        return merged


# Run main
if __name__ == "__main__":
    main()
