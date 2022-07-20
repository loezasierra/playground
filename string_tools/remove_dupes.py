# Remove duplicate words from a file of words
# Usage: remove_dupes.py <to_clean.txt> <outfile.txt>

from helpers import valid_usage, get_arg_file

## Constants ##
class constants:
    USAGE = "Usage: remove_dupes.py <to_clean.txt> <outfile.txt>"


"""
.txt file -> .txt file
Create a new text file where duplicate lines from given file are removed
ASSUME: file to be cleaned is sorted
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
    
    remove_dup_lines(infile, outfile)
    return


"""
String String -> .txt file
Create a new .txt file where all duplicate lines from infile are removed
ASSUME: infile is sorted
"""
def remove_dup_lines(infile, outfile):
    with open(infile, 'r') as f:
        words = f.read().splitlines()
    
    words = remove_dupes(words)
    
    with open(outfile, 'w') as f:
        for w in words:
            f.write(w)
            f.write('\n')
    return


"""
[listof String] -> [listof String]
Return the given list of words with duplicates removed
ASSUME: Words are sorted
ASSUME: List contains at least one word
"""
def remove_dupes(words):
    pop_count = 0
    i = 0
    n = len(words) - 1
    while i < n:
        if words[i] == words[i + 1]:
            words.pop(i)
            pop_count += 1
            n = len(words) - 1
        else:
            i += 1
    
    print(f"{pop_count} duplicates removed")
    return words

# Run main
if __name__ == '__main__':
    main()
