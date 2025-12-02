# !/bin/python3
# https://adventofcode.com/2025/day/2

import re
import sys
import logging

class ValidatorClass:
    
    def __init__( self ):
        self.invalid_ids = {}
    
    def add_invalid( self, id, tag ):
        if not tag in self.invalid_ids:
            self.invalid_ids[ tag ] = []
        self.invalid_ids[ tag ].append( id )

    def get_invalids( self ):
        return( self.invalid_ids )
    
    def sum_invalids( self ):
        sum=0
        for t in self.invalid_ids:
            for i in self.invalid_ids[t]:
                sum += int(i)
        return( sum )
    
    def print_invalids( self ):
        for t in self.invalid_ids:
            print(f"Bad Ids for {t}: {",".join( self.invalid_ids[t] )}")

    def check_valid( self, id, tag ):
        valid=True
        reason="Passed all checks"
        if (id[0] == "0"):
            valid=False
            reason="zero"
        elif (len(id) == 1):
            valid=True
            reason="length 1"
        else:
            # loop through lengths of digits. 
            # Can't repeat more than half the number, and if 
            # the length isn't evenly divisible with the match length,
            # it can't match
            length=len(id)
            for match_length in range( 1, int(length/2) + 1 ):
                if (length % match_length != 0):
                    continue
                # now march through the number looking for a match
                # skip the index we can't match
                matched=True
                for i in range( 0, length - match_length, match_length):
                    #logging.debug(f"Checking {id} dl={match_length} i={i}")
                    if id[i:i+match_length] != id[i+match_length:i+match_length*2]:
                        matched=False
                        break
                if (matched):
                    valid=False
                    reason=f"{id[0:match_length]} repeats"
        
        if not valid:
            self.add_invalid( id, tag )
            logging.debug(f"invalid, id={id}, reason=\"{reason}\"")
        return( valid )


def read_input( inputStream ):
    validator=ValidatorClass()
    invalid_count=0
    for line in inputStream:
        line=line.strip()
        if (len(line) == 0):
            continue
        ranges=line.split(",")
        for r in ranges:
            if r == "":
                continue
            logging.debug(f"r={r}")
            linematch=re.match(r"^(\d+)-(\d+)$",r)
            if (not linematch):
                raise Exception( f"*** line {r} not understood")
            
            low=int( linematch.group(1) )
            high=int( linematch.group(2) )
            for n in range( low, high+1):
                validator.check_valid( str(n), f"Line_{low}_{high}" )

    return( validator )

# main
if __name__ == '__main__':
    validator=read_input( sys.stdin )
    print(f"The sum of invalids is {validator.sum_invalids()}")

