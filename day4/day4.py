# !/bin/python3
# https://adventofcode.com/2025/day/4

import sys
import logging
import copy

class PaperClass:

    paper_marker='@'

    def __init__( self ):
        pass

    def count_adjacent( self, matrix, row, col ):
        count=0
        for r in range(max( row-1, 0), min( row+2, len( matrix ))):
            for c in range( max( col-1, 0), min( col+2, len(matrix[r]))):
                if (r == row and c == col):
                    continue
                if (matrix[r][c] == self.paper_marker):
                    count += 1
        return( count )
                       

    def find_available_rolls( self, matrix, max_rolls, do_update ):
        available_count=0
        for row in range( 0, len( matrix )):
            logging.debug(f"checking row[{row}]={"".join(matrix[row])}")
            print_row = copy.deepcopy( matrix[row] )
            for col in range( 0, len( matrix[row] )):
                if (matrix[row][col] == self.paper_marker):
                    roll_count=self.count_adjacent( matrix, row, col )
                    if (roll_count < max_rolls ):
                        available_count += 1 
                        print_row[col] = 'x'
                        if (do_update):
                            matrix[row][col] = 'x'
            logging.debug(f"found row={"".join(print_row)}")
        return( available_count )
    
def read_input( inputStream ):
    paper=PaperClass()
    matrix=[]
    first_line=True
    for line in inputStream:
        line=line.strip()
        if (len(line) == 0):
            continue
        if (first_line):
            expected_line_length=len( line )
        else:
            if (len( line ) != expected_line_length):
                raise Exception("Not expecting asymetrical lines")
            first_line = False
            
        matrix.append( list( line ) )
    
    
    sum_count=0
    last_sum=0
    sum=0
    while( True ): 
        sum = paper.find_available_rolls( matrix, 4, True )
        if (sum == last_sum):
            break
        sum_count += sum
        last_sum = sum

    return( sum_count )

# main
if __name__ == '__main__':
    print(f"Papers available are {read_input( sys.stdin )}")

