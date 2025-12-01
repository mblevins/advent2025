import sys
import pytest
import io
from  day1 import read_input

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
L5 
R60
L55
L1 
L99
R14
L82
'''


def test_sample_data():
    stream = io.StringIO(test_data_simple)
    assert (read_input( stream ) == 3)

def test_overflow_data():
    stream = io.StringIO(test_data_overflow)
    assert (read_input( stream ) == 3)
    
