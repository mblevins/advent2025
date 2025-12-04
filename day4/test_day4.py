import sys
import pytest
import io
from  day4 import read_input
import logging

test_data_sample = '''
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
'''

test_data_trivial = '''
..@@.@@@@.
@@@.@.@.@@
'''

def tesxt_trivial():
    stream = io.StringIO(test_data_trivial)
    sum=read_input( stream )
    assert(sum == 5)

def test_sample():
    stream = io.StringIO(test_data_sample)
    sum=read_input( stream )
    assert(sum == 13)

