import sys
import pytest
import io
from  day2 import read_input, ValidatorClass
import logging

test_data_sample = '''
11-22,95-115,
998-1012,
1188511880-1188511890,
222220-222224,
1698522-1698528,
446443-446449,
38593856-38593862,
565653-565659,
824824821-824824827,
2121212118-2121212124
'''


test_data_trivial = '''
11-22,
'''

def test_trivial():
    stream = io.StringIO(test_data_trivial)
    validator=read_input( stream )
    #validator.print_invalids()
    assert(validator.sum_invalids() == 33)

def test_sample():
    stream = io.StringIO(test_data_sample)
    validator=read_input( stream )
    #validator.print_invalids()
    assert( validator.sum_invalids() == 4174379265 )

