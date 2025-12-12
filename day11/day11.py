# !/bin/python3
# https://adventofcode.com/2025/day/7

import sys
import logging
import re
import copy
from collections import deque
from enum import Enum


class PathState( Enum ):
    PATH_UNKNOWN=1
    PATH_SUCCEEDED=2
    PATH_FAILED=3


class PathAttempt:

    def __init__( self, device, out):
        self.device=device
        self.out=out

    def id(self):
        return( f"{self.device}:{self.out}")

class DeviceClass:
    def __init__( self ):
        self.paths={}

    def add_line( self, device, outputs ):
        self.paths[device] = outputs

    # returns None, True or False
    def crossed_this_path( self, path_attempted, out ):
        for pa in path_attempted:
            if out in pa.history:
                return( pa.path_state )
        return( PathState.PATH_UNKNOWN )


    def find_out( self ):

        # both are list of PathAttempt's 
        paths_attempted=[]
        paths_todo=deque()

        for out in self.paths["you"]:
            paths_todo.append( out )

        successful_paths=0
        while (len( paths_todo ) > 0):
            node_name=paths_todo.pop()
            logging.debug(f"Popped {node_name}")
            for out in self.paths[node_name]:
                if (out == "out"):
                    logging.debug(" .. Success")
                    successful_paths += 1
                else:
                    paths_todo.append( out )
                    logging.debug(f" .. Adding {out}")

        return( successful_paths )
    
    

def read_input( inputStream, part):

    dc=DeviceClass()
    for line in inputStream:
        # device: device1 device2
        linematch=re.match(r"^(\w+): (.*)$", line)
        if not linematch:
            raise Exception("Unrecognized line:" + line )
        dc.add_line( linematch.group(1), linematch.group(2).split())

    if (part == 1):
        paths=dc.find_out()
    return( paths )

# main
if __name__ == '__main__':
    logging.basicConfig(level=getattr(logging, "DEBUG"))
    print(f"Number of paths is {read_input( sys.stdin, 1)}")

