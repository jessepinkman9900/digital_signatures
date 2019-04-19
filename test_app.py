import pytest
import random
import string

from dss import *

n = 4 # number of tests

def random_string(stringLength):
    """Generate a random string of given length"""
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

def test():
    for i in range(n):
        st = random_string(10)
        dso = DSS(st)
        h = dso.gen_hash()

        # Test for 1024 bits and e = 3
        dso.gen_keys(1024, 3)
        ds = dso.gen_DS(h)
        assert dso.verify(h, ds), "Test Failed"

        # Test for 1024 bit
        dso.gen_keys(1024)
        ds = dso.gen_DS(h)
        assert dso.verify(h, ds), "Test Failed"

        # Test for 2048 bit and e = 3
        dso.gen_keys(2048, 3)
        ds = dso.gen_DS(h)
        assert dso.verify(h, ds), "Test Failed"

        # Test for 2048 bit
        dso.gen_keys(2048)
        ds = dso.gen_DS(h)
        assert dso.verify(h, ds), "Test Failed"
