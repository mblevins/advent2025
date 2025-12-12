import sys
import pytest
import io
from  day11 import read_input
import numpy as np
import logging
import copy

test_data_sample = '''aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out'''


def test_sample_part1():
    stream = io.StringIO(test_data_sample)
    total=read_input( stream, 1 )
    assert(total == 5)







