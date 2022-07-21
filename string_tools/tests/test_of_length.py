# For testing ../of_length.py

import pytest
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from of_length import filter_words

class TestFilterWords:
    SINGLE_FOUR = ["good"]
    MANY_THREE  = ["all", "you", "the", "she"]
    MIXED = ["about", "all", "you", "come", "the", "they", "he", "she"]

    # Test single filtered in
    def test_single_in(self, tmp_path):
        # Setup input file
        infile = os.path.join(tmp_path, "in.txt")
        with open(infile, 'w') as f:
            for w in self.SINGLE_FOUR:
                f.write(w)
        
        # Setup output file path
        outfile = os.path.join(tmp_path, "out.txt")

        # Test
        filter_words(4, infile, outfile)

        with open (outfile, 'r') as f:
            words = f.read().splitlines()
        
        assert words == self.SINGLE_FOUR
    
    # Test single filtered out
    def test_single_out(self, tmp_path):
        # Setup input file
        infile = os.path.join(tmp_path, "in.txt")
        with open(infile, 'w') as f:
            for w in self.SINGLE_FOUR:
                f.write(w)
        
        # Setup output file path
        outfile = os.path.join(tmp_path, "out.txt")

        # Test
        filter_words(5, infile, outfile)

        with open(outfile, 'r') as f:
            words = f.read().splitlines()
        
        assert not words
    
    # Test many words where all are filtered in
    def test_many_in(self, tmp_path):
        # Setup input file
        infile = os.path.join(tmp_path, "in.txt")
        with open(infile, 'w') as f:
            for w in self.MANY_THREE:
                f.write(w)
                f.write('\n')
        
        # Setup output file path
        outfile = os.path.join(tmp_path, "out.txt")

        # Test
        filter_words(3, infile, outfile)

        with open(outfile, 'r') as f:
            words = f.read().splitlines()
        
        assert words == self.MANY_THREE
    
    # Test many word where some are filted out
    def test_many_out(self, tmp_path):
        # Setup input file
        infile = os.path.join(tmp_path, "in.txt")
        with open(infile, 'w') as f:
            for w in self.MIXED:
                f.write(w)
                f.write('\n')
        
        # Setup output file path
        outfile = os.path.join(tmp_path, "out.txt")

        # Test
        filter_words(3, infile, outfile)

        with open(outfile, 'r') as f:
            words = f.read().splitlines()

        assert words == self.MANY_THREE

# Run tests
if __name__ == '__main__':
    pytest.main(["-vv"])
