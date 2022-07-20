# For testing ../remove_dupes.py

import pytest
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from remove_dupes import remove_dup_lines, remove_dupes


class TestRemoveDupLines:
    NODUPES    = ["alpha", "beta", "charlie"]
    DUPLICATES = ["alpha", "alpha", "alpha", "beta", "beta", "charlie"]

    # Test set with no duplicates
    def test_nodupes(self, tmp_path):
        # Setup input file
        infile = os.path.join(tmp_path, "in.txt")
        with open(infile, 'w') as f:
            for s in self.NODUPES:
                f.write(s)
                f.write('\n')
        
        # Setup outfile file path
        outfile = os.path.join(tmp_path, "out.txt")

        # Test
        remove_dup_lines(infile, outfile)

        with open(outfile, 'r') as f:
            cleaned = f.read().splitlines()
        
        assert cleaned == self.NODUPES
    
    # Test set with duplicates
    def test_dupes(self, tmp_path):
        # Setup input file
        infile = os.path.join(tmp_path, "in.txt")
        with open(infile, 'w') as f:
            for s in self.DUPLICATES:
                f.write(s)
                f.write('\n')
        
        # Setup outfile file path
        outfile = os.path.join(tmp_path, "out.txt")

        # Test
        remove_dup_lines(infile, outfile)

        with open(outfile, 'r') as f:
            cleaned = f.read().splitlines()
        
        assert cleaned == self.NODUPES


class TestRemoveDupes:
    SINGLE = ["alpha"]
    SMALL_NODUPES = ["alpha"]
    SMALL_DUPES   = ["alpha", "alpha"]
    BIG_NODUPES = ["alpha", "beta", "charlie", "delta", "echo"]
    BIG_DUPES   = ["alpha", "alpha", "alpha", "beta", "beta", "charlie", "delta", "delta", "delta", "echo"]
    
    # Test single case
    def test_single(self):
        cleaned = remove_dupes(self.SINGLE)
        assert cleaned == self.SINGLE
    
    # Test small set with no duplicates
    def test_small_nodupes(self):
        cleaned = remove_dupes(self.SMALL_NODUPES)
        assert cleaned == self.SMALL_NODUPES
    
    # Test small set with duplicates
    def test_small_dupes(self):
        cleaned = remove_dupes(self.SMALL_DUPES)
        assert cleaned == self.SMALL_NODUPES
    
    # Test big set with no duplicates
    def test_big_nodupes(self):
        cleaned = remove_dupes(self.BIG_NODUPES)
        assert cleaned == self.BIG_NODUPES
    
    # Test big set with duplicates
    def test_big_dupes(self):
        cleaned = remove_dupes(self.BIG_DUPES)
        assert cleaned == self.BIG_NODUPES


# Run tests
if __name__ == '__main__':
    pytest.main()
