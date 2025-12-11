import sys
import pytest
import io
from  day10 import read_input
import numpy as np
import logging
import copy

test_data_sample = '''[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}'''


def test_sample_part1():
    stream = io.StringIO(test_data_sample)
    total=read_input( stream, 1 )
    assert(total == 7)







