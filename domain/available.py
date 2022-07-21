# Available domain name script
# Usage: available.py <words.txt> <outfile.txt>

import sys
import os.path
from whois import whois

## Constants ##
class constants:
    USAGE = "Usage: available.py <words.txt> <outfile.txt>"


"""
.txt file -> .txt file
Create a new text file of available .com domains from given file
"""
def main():
    if not valid_usage():
        return
    
    infile = get_infile()
    if not infile:
        return
    
    outfile = get_outfile()
    if not outfile:
        return
    
    available_domains(infile, outfile)
    return


"""
None -> Bool
Return true if given 2 additional command line arguments
"""
def valid_usage():
    if len(sys.argv) != 3:
        print(constants.USAGE)
        return False
    return True


"""
None -> Stirng or False
Return first argument name if file is of .txt, exists, and is nonempty
        Return False otherwise
"""
def get_infile():
    file = sys.argv[1]

    # Check valid file type
    if not file.endswith(".txt"):
        print(f"File {file} must be of type .txt")
        print(constants.USAGE)
        return False
    
    # Check file exists
    if not os.path.exists(file):
        print(f"File {file} does not exist")
        print(constants.USAGE)
        return False
    
    # Check file is not empty
    if not os.path.getsize(file) > 0:
        print(f"File {file} is empty")
        print(constants.USAGE)
        return False
    
    return file


"""
None -> String or False
Return and clear second argument if file is of .txt
        Return False otherwise
"""
def get_outfile():
    file = sys.argv[2]

    # Check valid file type
    if not file.endswith(".txt"):
        print(f"File {file} must be of type .txt")
        print(constants.USAGE)
        return False
    
    # Clear file
    open(file, 'w').close()

    return file


"""
String String -> .txt file
Create a new .txt file of available .com domains from given file
"""
def available_domains(infile, outfile):
    with open(infile, 'r') as f:
        words = f.read().splitlines()
    
    words = filter(com_available, words)
    
    with open(outfile, 'w') as f:
        for w in words:
            f.write(w)
            f.write('\n')
    return


"""
String -> Bool
Return true if string is avilable as a .com domain
"""
def com_available(word):
    domain = word + ".com"

    try:
        whois(domain)
    except:
        print(f"{domain} is available")
        return True
    else:
        print(f"{domain} is unavailable")
        return False



# Run  main
if __name__ == '__main__':
    main()
