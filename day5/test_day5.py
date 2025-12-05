import sys
import pytest
import io
from  day5 import read_input
import logging

test_data_sample = '''3-5
10-14
16-20
12-18

1
5
8
11
17
32'''


test_data_corners= '''3-5
10-14
16-20
12-22
13-14
25-37

1
5
8
11
17
21
32'''




def test_sample_part1():
    stream = io.StringIO(test_data_sample)
    sum=read_input( stream, "part1" )
    assert(sum == 3)

def test_corners_part1():
    stream = io.StringIO(test_data_corners)
    sum=read_input( stream, "part1" )
    assert(sum == 5)

def test_sample_part2():
    stream = io.StringIO(test_data_sample)
    sum=read_input( stream, "part2" )
    assert(sum == 14)

