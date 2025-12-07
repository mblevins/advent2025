# !/bin/python3
# https://adventofcode.com/2025/day/6

import sys
import logging
import math
from  enum import Enum
import numpy as np


class ColumnClass:
    def __init__( self, start_pos, length, operator ):
        self.start_pos=start_pos
        self.length=length
        self.operator=operator
        self.id=f"{start_pos}/{length}/{operator}"
 
class ProblemClass:

    def __init__( self, matrix  ):
        self.cell_array = np.asanyarray( matrix[0:len(matrix)-1] )
        num_rows=self.cell_array.shape[0]
        num_cells=self.cell_array.shape[1]   

        # probably a better way of doing the next line, but it works
        operators="".join( matrix[len(matrix)-1] ).split()

        # Build the column index for groups that end in blanks
        self.columns=[]
        start_cell=0
        cell_i=0
        for cell_i in range( 0, num_cells ):
            # every cell in a column is blank is our column termination
            if (list(self.cell_array[:,cell_i]).count(' ') == num_rows):
                self.columns.append( ColumnClass( start_cell, cell_i-start_cell, operators[len( self.columns)] ) )
                start_cell=cell_i+1
        # Add the column we're looking at, it doesn't end in a blank
        self.columns.append( ColumnClass( start_cell, num_cells-start_cell, operators[len( self.columns)] ) )

    def get_simple_vector( self, col ):
        vector=[]
        num_rows=self.cell_array.shape[0]
        for r in range( 0, num_rows ):
            num="".join( self.cell_array[r][col.start_pos:col.start_pos+col.length] )
            vector.append( int(num) )
        return( vector )
    
    def get_reversed_vector( self, col ):
        vector=[]
        for ci in range( col.start_pos+col.length-1, col.start_pos-1, -1 ):
            num="".join( self.cell_array[:,ci] )
            vector.append( int(num) )
        return( vector )


    def total( self, part):
        total=0
        for col in self.columns:
            if (part == 1):
                operand_vector=self.get_simple_vector( col )
            elif (part == 2):
                operand_vector=self.get_reversed_vector( col )
            else:
                raise Exception("Unknown problem part \"{part}\"")
            if (col.operator == '+' ):
                subtotal=sum( operand_vector )
            elif (col.operator == '*'):
                subtotal=math.prod( operand_vector )
            else:
                raise Exception(f"Internal error, unknown op {col.operator}")
            logging.debug(f"Column subtotal is {subtotal}")
            total += subtotal
            
        return( total )
            
def read_input( inputStream, part):
    matrix=[]
    for line in inputStream:
        chars=list(line.rstrip("\n"))
        matrix.append( chars )

    problems=ProblemClass( matrix )
    return( problems.total( part ) )

# main
if __name__ == '__main__':
    logging.basicConfig(level=getattr(logging, "DEBUG"))
    print(f"Total Operations are {read_input( sys.stdin, 2 )}")

