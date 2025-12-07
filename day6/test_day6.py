import sys
import pytest
import io
from  day6 import read_input
import logging
import numpy as np

test_data_sample = '''123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +'''

#           1
# 012345678901234
# 123 328  51 64 
#  45 64  387 23 
#   6 98  215 314
# *   +   *   +
#

def test_sample_part1():
    stream = io.StringIO(test_data_sample)
    sum=read_input( stream, 1 )
    assert(sum == 4277556)

def test_sample_part2():
    stream = io.StringIO(test_data_sample)
    sum=read_input( stream, 2 )
    assert(sum == 3263827)

        


