# !/bin/python3
# https://adventofcode.com/2025/day/6

import sys
import logging
import re
from  enum import Enum
import numpy as np

MAX_DIGITS=5

class ProblemClass:

    ALLOWED_OPERATIONS=['+','*']

    def __init__( self, str_matrix ):
        if (len(str_matrix) < 3):
            raise Exception(f"Expecting at least 3 lines")
        self.operand_str_array = np.asarray( str_matrix[0:len(str_matrix)-1] )

        last_line=len(str_matrix)-1
        self.operation_vector=[]
        for c in range(0, len(str_matrix[last_line])):
            operation=str_matrix[last_line][c]
            if operation not in self.ALLOWED_OPERATIONS:
                raise Exception(f"Unknown operation in column {c}, op={operation}")
            self.operation_vector.append( operation )

    def total( self ):
        total=0
        operand_int_array=self.operand_str_array.astype(int)
        cols=self.operand_str_array.shape[1]
        for c in range( 0, cols ):
            op = self.operation_vector[c]
            if (op == '+' ):
                subtotal=np.sum( operand_int_array[:,c] )
            elif (op == '*'):
                subtotal=np.prod( operand_int_array[:,c] )
            else:
                raise Exception(f"Internal error, unknown op {op}")
            logging.debug(f"Subtotal for col {c} is {subtotal}")
            total += subtotal
            
        return( total )


def split_line( line ):
    items=[]
    curDigit=""
    for si in range(0, len(line)):
        c=line[si]
        logging.debug(f"c={c}")
        if (c.isdigit()):
            curDigit += c
        else:
            logging.debug(f"Adding curDigit {curDigit}")
            items.append( curDigit )
            curDigit=""
    items.append( curDigit )
    return( items )
            
def read_input( inputStream, part):
    matrix=[]
    for line in inputStream:
        items=split_line(line.rstrip("\n"))
        logging.debug(f"line=\"{line}\", items={items}")
        matrix.append( items)

    problems=ProblemClass( matrix )
    if (part == 2):
        matrix = problems.transform_matrix( )
    return( problems.total() )

# main
if __name__ == '__main__':
    print(f"Total Operations are {read_input( sys.stdin, 2 )}")

