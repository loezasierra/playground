# Helpers for sting tool programs

import sys
import os.path


def valid_usage(argument_count=1, message="Invalid usage"):
    """
    Int String -> Bool
    Return true if desired number of command line arguments are given. Otherwise print message.
    """
    if len(sys.argv) != argument_count:
        print(message)
        return False
    return True


def get_arg_file(n = 0, message=False, extension=False, mustexist=False, nonempty=False, clear=False):
    """
    Int -> String or False
    Return the name of the file from the nth command line argument
        Extension ensures the argument ends with given file extension
        MustExist ensures the file exists
        NonEmpty ensures the file is not emtpy
        Clear clears the file of contents
    """
    arg = sys.argv[n]

    # Check valid file type
    if extension:
        if not arg.endswith(extension):
            print(f"File {arg} must be of type {extension}")
            if message:
                print(message)
            return False
    
    # Check file exists
    if mustexist:
        if not os.path.exists(arg):
            print(f"File {arg} does not exist")
            if message:
                print(message)
            return False
    
    # Check file is not empty
    if nonempty:
        if not os.path.getsize(arg) > 0:
            print(f"File {arg} is empty")
            if message:
                print(message)
            return False
    
    # Clear file
    if clear:
        open(arg, 'w').close()

    return arg
