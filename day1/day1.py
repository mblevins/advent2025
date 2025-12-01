# !/bin/python3
# https://adventofcode.com/2025/day/1

import re
import sys
import logging

class DialClass:
    # Note: since we're just counting zeros, there's no
    # need to track turn under/overflows
    DIAL_MAX=100

    def __init__( self ):
        self.pos=50
        self.num_zero_pos=0

    def turn( self, dir, clicks ):
        if (dir == "L"):
            self.pos = self.pos - clicks
        elif (dir == "R"):
            self.pos = self.pos + clicks
        else:
            raise Exception( f"*** Internal error, *turn* called with dir={dir}")

        logging.debug( f"DialClass.turn, dir={dir}, clicks={clicks}, pos={self.pos}")
        if (self.pos % self.DIAL_MAX == 0):
                self.num_zero_pos = self.num_zero_pos + 1

    def get_num_zeros( self ):
        return( self.num_zero_pos )

def read_input( inputStream ):
    dial=DialClass()
    for line in inputStream:
        line=line.strip()
        if (len(line) == 0):
            continue
        logging.debug( f"Line={line}" )
        linematch=re.match(r"^([LR])(\d+)$",line)
        if (not linematch):
            raise Exception( f"*** line {line} not understood")
        dial.turn( linematch.group(1), int(linematch.group(2)))
    return( dial.get_num_zeros() )

# main
if __name__ == '__main__':
    num_zeros=read_input( sys.stdin )
    print(f"The number of times zero was landed on was {num_zeros}")
