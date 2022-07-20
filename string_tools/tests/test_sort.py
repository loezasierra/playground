# For testing ../sort.py

import pytest
import os
import sys
from random import shuffle

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from sort import sort_lines, sort_words


class TestSortLines:
    SORTED = ["alpha", "beta", "charlie", "delta"]
    UNSORTED = ["beta", "alpha", "delta", "charlie"]

    # Test sorted set
    def test_sorted(self, tmp_path):
        # Setup input file
        infile = os.path.join(tmp_path, "in.txt")
        with open(infile, 'w') as f:
            for s in self.SORTED:
                f.write(s)
                f.write('\n')
        
        # Setup output file path
        outfile = os.path.join(tmp_path, "out.txt")

        # Test
        sort_lines(infile, outfile)

        with open(outfile, 'r') as f:
            sorted = f.read().splitlines()
        
        assert sorted == self.SORTED
    
    # Test unsorted set
    def test_unsorted(self, tmp_path):
        # Setup input file
        infile = os.path.join(tmp_path, "in.txt")
        with open(infile, 'w') as f:
            for s in self.UNSORTED:
                f.write(s)
                f.write('\n')
        
        # Setup output file path
        outfile = os.path.join(tmp_path, "out.txt")

        # Test
        sort_lines(infile, outfile)

        with open(outfile, 'r') as f:
            sorted = f.read().splitlines()
        
        assert sorted == self.SORTED


class TestSortWords:
    SINGLE = ["alpha"]

    def shuffle_copy(l): 
        """ Return shuffled copy of list """
        copy = l.copy()
        shuffle(copy)
        return copy

    SMALL_SORTED = ["alpha", "beta", "charlie"]
    SMALL_UNSORTED = shuffle_copy(SMALL_SORTED)
    BIG_SORTED = ["a", "all", "as", "at", "be", "because", "go", "go", "good", "he", "her", "him", "his", "year", "you", "your"]
    BIG_UNSORTED = shuffle_copy(BIG_SORTED)
    
    # Test single case
    def test_base(self):
        sorted = sort_words(self.SINGLE)
        assert sorted == self.SINGLE
    
    # Test small sorted set
    def test_small_sorted(self):
        sorted = sort_words(self.SMALL_SORTED)
        assert sorted == self.SMALL_SORTED
    
    # Test small unsorted set
    def test_small_unsorted(self):
        sorted = sort_words(self.SMALL_UNSORTED)
        assert sorted == self.SMALL_SORTED
    
    # Test big sorted set
    def test_big_sorted(self):
        sorted = sort_words(self.BIG_SORTED)
        assert sorted == self.BIG_SORTED
    
    # Test big unsorted set
    def test_big_unsorted(self):
        sorted = sort_words(self.BIG_UNSORTED)
        assert sorted == self.BIG_SORTED


# Run tests
if __name__ == '__main__':
    pytest.main()
