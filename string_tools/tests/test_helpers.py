# For testing ../helpers.py

import pytest
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from helpers import constants, valid_usage, get_arg_file


class TestValidUsage:
    invalid_usage = constants.INVALID_USAGE + '\n'

    # Test too little arguments
    def test_too_little(self, capsys):
        sys.argv = ["helpers.py"]

        return_val = valid_usage(2)
        captured = capsys.readouterr().out
        assert return_val == False
        assert captured == self.invalid_usage
    
    # Test too many arguments
    def test_too_many(self, capsys):
        sys.argv = ["helpers.py", "file1.csv", "file2.txt"]

        return_val = valid_usage(2)
        captured = capsys.readouterr().out
        assert return_val == False
        assert captured == self.invalid_usage

    # Test correct message output
    def test_message(self, capsys):
        sys.argv = ["helpers.py", "file.txt"]

        return_val = valid_usage(1, "Usage: helpers.py")
        captured = capsys.readouterr().out
        correct_out = "Usage: helpers.py\n"
        assert return_val == False
        assert captured == correct_out

    # Test correct number of arguments
    def test_correct(self):
        sys.argv = ["helpers.py", "file.txt"]

        return_val = valid_usage(2)
        assert return_val == True


class TestGetArgFile:
    mess = "Usage: helpers.py <file.py>"
    
    # Test simple return value
    def test_simple(self):
        sys.argv = ["helpers.py", "file.txt"]

        return_val = get_arg_file(1)
        assert return_val == "file.txt"

    # Test no file extension with no message
    def test_noexten_nomess(self, capsys):
        sys.argv = ["helpers.py", "file"]

        return_val = get_arg_file(1, extension=".txt")
        captured = capsys.readouterr().out
        correct_out = constants.INVALID_EXTENSION.format("file", ".txt") + '\n'
        assert return_val == False
        assert captured == correct_out
    
    # Test incorrect file extension with no message
    def test_badexten_nomess(self, capsys):
        sys.argv = ("helpers.py", "file.csv")

        return_val = get_arg_file(1, extension=".txt")
        captured = capsys.readouterr().out
        correct_out = constants.INVALID_EXTENSION.format("file.csv", ".txt") + '\n'
        assert return_val == False
        assert captured == correct_out
    
    # Test incorrect file extension with a message
    def test_badexten(self, capsys):
        sys.argv = ("helpers.py", "file.csv")

        return_val = get_arg_file(1, self.mess, ".txt")
        captured = capsys.readouterr().out
        correct_out = constants.INVALID_EXTENSION.format("file.csv", ".txt")        \
                        + '\n'                                                      \
                        + self.mess                                                 \
                        + '\n'
        assert return_val == False
        assert captured == correct_out
    
    # Test correct file extension with no message
    def test_exten_nomess(self, capsys):
        sys.argv = ["helpers.py", "file.txt"]

        return_val = get_arg_file(1, extension=".txt")
        captured = capsys.readouterr().out
        assert return_val == "file.txt"
        assert not captured
    
    # Test correct file extension with a message (message should not print)
    def test_exten(self, capsys):
        sys.argv = ["helpers.py", "file.txt"]

        return_val = get_arg_file(1, self.mess, ".txt")
        captured = capsys.readouterr().out
        assert return_val == "file.txt"
        assert not captured
    
    # Test file does not exist with no message
    def test_noexist_nomess(self, capsys):
        sys.argv = ["helpers.py", "file.txt"]

        return_val = get_arg_file(1, mustexist=True)
        captured = capsys.readouterr().out
        correct_out = constants.FILE_NONEXIST.format("file.txt") + '\n'
        assert return_val == False
        assert captured == correct_out
    
    # Test file does not exist with a messaage
    def test_noexist(self, capsys):
        sys.argv = ["helpers.py", "file.txt"]

        return_val = get_arg_file(1, self.mess, mustexist=True)
        captured = capsys.readouterr().out
        correct_out = constants.FILE_NONEXIST.format("file.txt")        \
                        + '\n'                                          \
                        + self.mess                                     \
                        + '\n'
        assert return_val == False
        assert captured == correct_out
    
    # Test file exists with no message
    def test_exist_nomess(self, capsys, tmp_path):
        # Create test file
        file = os.path.join(tmp_path, "file.txt")
        open(file, 'w').close()

        # Test 
        sys.argv = ["helpers.py", file]

        return_val = get_arg_file(1, mustexist=True)
        captured = capsys.readouterr().out

        assert return_val == file
        assert not captured
    
    # Test file exists with message (message should not print)
    def test_exist(self, capsys, tmp_path):
        # Create test file
        file = os.path.join(tmp_path, "file.txt")
        open(file, 'w').close()

        # Test
        sys.argv = ["helpers.py", file]

        return_val = get_arg_file(1, self.mess, mustexist=True)
        captured = capsys.readouterr().out

        assert return_val == file
        assert not captured

    # Test file is empty with no message
    def test_empty_nomess(self, capsys, tmp_path):
        # Create test file
        file = os.path.join(tmp_path, "file.txt")
        open(file, 'w').close()

        # Test
        sys.argv = ["helpers.py", file]

        return_val = get_arg_file(1, nonempty=True)
        captured = capsys.readouterr().out
        correct_out = constants.FILE_NONEMPTY.format(file) + '\n'
        assert return_val == False
        assert captured == correct_out
    
    # Test file is empty with message
    def test_empty(self, capsys, tmp_path):
        # Create test file
        file = os.path.join(tmp_path, "file.txt")
        open(file, 'w').close()

        # Test
        sys.argv = ["helpers.py", file]

        return_val = get_arg_file(1, self.mess, nonempty=True)
        captured = capsys.readouterr().out
        correct_out = constants.FILE_NONEMPTY.format(file)         \
                        + '\n'                                     \
                        + self.mess                                \
                        + '\n'
        assert return_val == False
        assert captured == correct_out
    
    # Test file nonempty with no message
    def test_noempty_nomess(self, capsys, tmp_path):
        # Create test file
        file = os.path.join(tmp_path, "file.txt")
        with open(file, 'w') as f:
            f.write("hello, world")
        
        # Test
        sys.argv = ["helpers.py", file]

        return_val = get_arg_file(1, nonempty=True)
        captured = capsys.readouterr().out
        assert return_val == file
        assert not captured
    
    # Test file nonempty with message (message should not print)
    def test_noempty(self, capsys, tmp_path):
        # Create test file
        file = os.path.join(tmp_path, "file.txt")
        with open(file, 'w') as f:
            f.write("hello, world")
        
        # Test
        sys.argv = ["helpers.py", file]

        return_val = get_arg_file(1, self.mess, nonempty=True)
        captured = capsys.readouterr().out
        assert return_val == file
        assert not captured
    
    # Test clearing a file that does not exist
    def test_clear_nonexist(self, capsys, tmp_path):
        # Create test path
        file = os.path.join(tmp_path, "file.txt")

        # Test
        sys.argv = ["helpers.py", file]

        return_val = get_arg_file(1, clear=True)
        captured = capsys.readouterr().out
        assert os.path.exists(file)
        assert os.path.getsize(file) == 0
        assert return_val == file
        assert not captured
    
    # Test clearing an empty file
    def test_clear_empty(file, capsys, tmp_path):
        # Create file to be cleared
        file = os.path.join(tmp_path, "file.txt")
        open(file, 'w').close()

        # Test
        sys.argv = ["helpers.py", file]

        return_val = get_arg_file(1, clear=True)
        captured = capsys.readouterr().out
        assert os.path.exists(file)
        assert os.path.getsize(file) == 0
        assert return_val == file
        assert not captured
    
    # Test clearing a file of with contents
    def test_clear(file, capsys, tmp_path):
        # Create file to be cleared
        file = os.path.join(tmp_path, "file.txt")
        with open(file, 'w') as f:
            f.write("hello, world")
        
        # Test
        sys.argv = ["helpers.py", file]

        return_val = get_arg_file(1, clear=True)
        captured = capsys.readouterr().out
        assert os.path.exists(file)
        assert os.path.getsize(file) == 0
        assert return_val == file
        assert not captured


# Run tests
if __name__ == '__main__':
    pytest.main()
