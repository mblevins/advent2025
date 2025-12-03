import sys
import pytest
import io
from  day3 import read_input
import logging

test_data_sample = '''
987654321111111
811111111111119
234234234234278
818181911112111
'''

test_data_trivial = '''
811111111111119
'''

def test_trivial():
    stream = io.StringIO(test_data_trivial)
    sum=read_input( stream )
    assert(sum == 89)

def test_sample():
    stream = io.StringIO(test_data_sample)
    sum=read_input( stream )
    assert(sum == 357)

