# !/bin/python3
# https://adventofcode.com/2025/day/5

import sys
import logging
import re
from  enum import Enum


class RangeClass:

    def __init__( self, low, high ):
        self.low = low
        self.high = high
        self.optimized_out = False

    def optimize_out( self ):
        self.optimized_out = True

class IngredientClass:

    def __init__( self ):
        # array of dicts, with low/high entries
        self.fresh_ranges=[]

    def add_range( self, low, high ):
        logging.debug(f"Adding {low}/{high}")
        self.fresh_ranges.append( RangeClass( low, high ) )

    def combine_ranges( self ):
        sorted_ranges = sorted(self.fresh_ranges, key=lambda r: r.low) 
        for ri in range( 0, len( sorted_ranges ) - 1):
            # the next low must be higher, since we sorted, so if the high is less it means we're overlapping
            logging.debug(f"Checking {sorted_ranges[ri].low}-{sorted_ranges[ri].high} against {sorted_ranges[ri+1].low}-{sorted_ranges[ri+1].high}")
            if (sorted_ranges[ri].high >= sorted_ranges[ri+1].low):
                new_range_low=sorted_ranges[ri].low
                new_range_high=max( sorted_ranges[ri].high, sorted_ranges[ri+1].high )
                logging.debug(f".. adjusting {sorted_ranges[ri+1].low}-{sorted_ranges[ri+1].high} to be {new_range_low}-{new_range_high}")      
                sorted_ranges[ri+1].low = new_range_low
                sorted_ranges[ri+1].high = new_range_high
                sorted_ranges[ri].optimize_out()
        
        # compact
        # probably some cool lambda for this
        self.fresh_ranges=[]
        for r in sorted_ranges:
            if (not r.optimized_out):
                logging.debug(f"Adding combined range {r.low}-{r.high}")
                self.fresh_ranges.append( r )
    
    def sum_ranges( self ):
        sum=0
        for r in self.fresh_ranges:
            sum += r.high - r.low + 1
        return( sum )

    def is_fresh( self, ingredient ):
        for r in self.fresh_ranges:
            logging.debug(f"Checking if {ingredient} is in range {r.low}/{r.high}")
            if (ingredient >= r.low and ingredient <= r.high):
                logging.debug(f" .. yep")
                return( True )
        logging.debug(f"{ingredient} wasn't in any ranges")
        return( False )

    
def read_input( inputStream, part):
    ingredeints=IngredientClass()

    class ReadState( Enum ):
        READING_RANGE=0
        READING_INGREDIENTS=1
    
    state=ReadState.READING_RANGE
    
    sum=0
    for line in inputStream:
        line=line.strip()
        if (state == ReadState.READING_RANGE ):
            if (len(line) == 0):
                ingredeints.combine_ranges()
                if (part == "part1"):
                    state = ReadState.READING_INGREDIENTS
                else:
                    break
            else:
                linematch=re.match(r"^(\d+)-(\d+)$",line)
                if (not linematch):
                    raise Exception( f"*** line {line} not understood")
                ingredeints.add_range( int(linematch.group(1)), int(linematch.group(2)))
        
        elif (state == ReadState.READING_INGREDIENTS):
            if (ingredeints.is_fresh( int( line ) ) ):
                sum +=1

    if (part == "part2"):
        sum=ingredeints.sum_ranges()

    return( sum )

# main
if __name__ == '__main__':
    print(f"Number of fresh ingredients are {read_input( sys.stdin, "part2" )}")

