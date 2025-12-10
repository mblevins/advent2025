import sys
import pytest
import io
from  day9 import read_input
import numpy as np
import logging

test_data_sample = '''7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3'''

# per https://www.reddit.com/r/adventofcode/comments/1pi5rqn/2025_day_9_part_2_check_your_solution_with_this/
test_data_cursed_1 = '''1,0
3,0
3,6
16,6
16,0
18,0
18,9
13,9
13,7
6,7
6,9
1,9'''


#   01234567890123
# 0 ..............
# 1 .......#...#..
# 2 ..............
# 3 ..#....#......
# 4 ..............
# 5 ..#......#....
# 6 ..............
# 7 .........#.#..
# 8 ..............
#
# Y,X coords
# UR=4,3
# UL=11,1
# LR=2,5
# LL=1,7


#   01234567890123
# 0 ..............
# 1 .......#...#..
# 2 ..............
# 3 ..#....#......
# 4 ..............
# 5 ..#......#....
# 6 ..............
# 7 .........#.#..
# 8 ..............
#
# Y,X coords
# UR=4,3
# UL=11,1
# LR=2,5
# LL=1,7


def test_sample_part1():
    stream = io.StringIO(test_data_sample)
    total=read_input( stream, 1 )
    assert(total == 50)

def xtest_sample_part2_cursed():
    stream = io.StringIO(test_data_cursed_1)
    total=read_input( stream, 1 )
    assert(total == 30)



