import sys
import pytest
import io
from  day8 import read_input
import numpy as np
import logging

test_data_sample = '''162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689'''

def test_sample_part1():
    stream = io.StringIO(test_data_sample)
    total=read_input( stream, 1, 10 )
    assert(total == 40)

def test_sample_part2():
    stream = io.StringIO(test_data_sample)
    total=read_input( stream, 2, 0 )
    assert(total == 25272)


