# !/bin/python3
# https://adventofcode.com/2025/day/1

import re
import sys
import logging

class DialClass:
    DIAL_MAX=100

    def __init__( self ):
        self.pos=50
        self.num_simple_zeros=0
        self.num_any_zeros=0

    def turn( self, clicks ):

        # makes it easier if we normalize
        num_extra_turns=abs(int( clicks / self.DIAL_MAX ))
        if (clicks > 0):
            clicks=clicks - num_extra_turns * self.DIAL_MAX
        else:
            clicks=clicks + num_extra_turns * self.DIAL_MAX

        new_pos = self.pos + clicks

        did_rotate=False   
        # landing on zero is a special case, else check if we're high or low
        if (new_pos % self.DIAL_MAX == 0):
            self.num_simple_zeros = self.num_simple_zeros + 1
            self.num_any_zeros = self.num_any_zeros + 1
            new_pos = 0
        else: 
            if (new_pos < 0):
                did_rotate=True
                new_pos=new_pos + self.DIAL_MAX 
            elif (new_pos >= self.DIAL_MAX):
                did_rotate=True
                new_pos=new_pos - self.DIAL_MAX 

            # if we start on zero, it isn't a real rotation
            if (did_rotate and self.pos != 0):
                self.num_any_zeros = self.num_any_zeros + 1 

        self.num_any_zeros = self.num_any_zeros + num_extra_turns
            

        logging.debug( f"DialClass.turn, clicks={clicks}, pos={self.pos}, " +
                       f"num_extra_turns={num_extra_turns}, new_pos={new_pos}, did_rotate={did_rotate}, " +
                       f"num_simple_zeros={self.num_simple_zeros}, num_any_zero={self.num_any_zeros}")
        
        self.pos = new_pos

    def get_simple_zeros( self ):
        return( self.num_simple_zeros )
    
    def get_any_zeros( self ):
        return( self.num_any_zeros )

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
        if (linematch.group(1) == "L"):
            clicks = - int(linematch.group(2))
        else:
            clicks = int(linematch.group(2))      
        dial.turn( clicks )
    return( dial )

# main
if __name__ == '__main__':
    dial=read_input( sys.stdin )
    print(f"The number of times zero was landed on was {dial.get_simple_zeros()}")
    print(f"The number of times zero was passed on was {dial.get_any_zeros()}")
