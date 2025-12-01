import sys
import pytest
import io
from  day1 import read_input, DialClass

test_data_simple = '''
L68
L30 
R48
L5 
R60
L55
L1 
L99
R14
L82
'''

test_data_overflow = '''
L68
L130 
R248
L505 
R60
L55
L1 
L99
R14
L82
'''

test_data_trivial = '''
R1000
'''


def test_sample_data_part1():
    stream = io.StringIO(test_data_simple)
    assert (read_input( stream ).get_simple_zeros() == 3)


def test_overflow_data_part1():
    stream = io.StringIO(test_data_overflow)
    assert (read_input( stream ).get_simple_zeros() == 3)
    

def test_sample_data_part2():
    stream = io.StringIO(test_data_simple)
    assert (read_input( stream ).get_any_zeros() == 6)

def test_overflow_data_part2():
    stream = io.StringIO(test_data_overflow)
    assert (read_input( stream ).get_any_zeros() == 14)
    
def test_trivial_data():
    stream = io.StringIO(test_data_trivial)
    assert (read_input( stream ).get_any_zeros() == 10)