# For testing ../available.py

import pytest
import os
import sys

currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from available import available_domains, com_available


class TestAvailableDomains:
    SINGLE_AVAILABLE   = "hyuqazkdec"
    SINGLE_UNAVAILABLE = "google"

    MIXED = ["google", "hyuqazkdec", "apple", "fkrovmwsx", "netfilx"]
    MIXED_AVAILABLE = ["hyuqazkdec", "fkrovmwsx"]

    # Test single available domain
    def test_single_available(self, tmp_path):
        # Setup infile
        infile = os.path.join(tmp_path, "in.txt")
        with open(infile, 'w') as f:
            f.write(self.SINGLE_AVAILABLE)
        
        # Setup outfile file path
        outfile = os.path.join(tmp_path, "out.txt")

        # Test
        available_domains(infile, outfile)

        with open(outfile, 'r') as f:
            domains = f.read().splitlines()
        
        assert domains == [self.SINGLE_AVAILABLE]
    
    # Test single unavailable domain
    def test_single_unavailable(self, tmp_path):
        # Setup infile
        infile = os.path.join(tmp_path, "in.txt")
        with open(infile, 'w') as f:
            f.write(self.SINGLE_UNAVAILABLE)
        
        # Setup outfile file path
        outfile = os.path.join(tmp_path, "out.txt")

        # Test
        available_domains(infile, outfile)

        with open(outfile, 'r') as f:
            domains = f.read().splitlines()
        
        assert not domains
    
    # Test list of mixed domains
    def test_mixed(self, tmp_path):
        # Setup infile
        infile = os.path.join(tmp_path, "in.txt")
        with open(infile, 'w') as f:
            for w in self.MIXED:
                f.write(w)
                f.write('\n')
        
        # Setup outfile file path
        outfile = os.path.join(tmp_path, "out.txt")

        # Test
        available_domains(infile, outfile)

        with open(outfile, 'r') as f:
            domains = f.read().splitlines()
        
        assert domains == self.MIXED_AVAILABLE


class TestComAvailable:
    AVAILABLE = "hyuqazkdec"
    UNAVAILABLE = "google"

    # Test available domain
    def test_available(self):
        a = com_available(self.AVAILABLE)
        assert a == True
    
    # Test unavailable domain
    def test_unavailable(self):
        a = com_available(self.UNAVAILABLE)
        assert a == False


# Run tests
if __name__ == '__main__':
    pytest.main(["-vv"])
