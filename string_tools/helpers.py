# Helpers for sting tool programs

import sys
import os.path

class constants:
    # for valid_usage
    INVALID_USAGE = "Invalid usage"

    # for get_arg_file
    INVALID_EXTENSION = "File {} must be of type {}"
    FILE_NONEXIST = "File {} does not exist"
    FILE_NONEMPTY = "File {} is empty"


def valid_usage(argument_count=1, message=constants.INVALID_USAGE):
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
            print(constants.INVALID_EXTENSION.format(arg, extension))
            if message:
                print(message)
            return False
    
    # Check file exists
    if mustexist:
        if not os.path.exists(arg):
            print(constants.FILE_NONEXIST.format(arg))
            if message:
                print(message)
            return False
    
    # Check file is not empty
    if nonempty:
        if not os.path.getsize(arg) > 0:
            print(constants.FILE_NONEMPTY.format(arg))
            if message:
                print(message)
            return False
    
    # Clear file
    if clear:
        open(arg, 'w').close()

    return arg
