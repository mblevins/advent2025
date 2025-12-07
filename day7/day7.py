# !/bin/python3
# https://adventofcode.com/2025/day/7

import sys
import logging
from  enum import Enum

 
class Timeline:

    def __init__( self ):
        self.history=""

class TacyonClass:

    def __init__( self, matrix  ):
        self.splitter_line = matrix[0]
        self.splitter_matrix = matrix[1:]
        self.num_splitter_rows = len( matrix )-1
        self.num_cols = len( matrix[0])
        self.done_searches={}
        for cols in matrix:
            if len(cols) != self.num_cols:
                raise Exception("Asymetrical splitter lines")


    def total_part1( self ):
        cur_stream_locs=[]
        # raises exception if now found, so no need to check
        cur_stream_locs.append(self.splitter_line.index('S'))
        
        num_splits=0
        for ri in range( 0, self.num_splitter_rows ):
            #logging.debug(f"Checking row {ri}")
            next_stream_locs=[]
            for stream_loc in cur_stream_locs:
                if (self.splitter_matrix[ri][stream_loc] == '^'):
                    if (stream_loc > 0 and not (stream_loc-1) in next_stream_locs):
                        next_stream_locs.append( stream_loc -1 )
                    if (stream_loc < self.num_cols - 1 and not (stream_loc+1) in next_stream_locs):
                        next_stream_locs.append( stream_loc + 1 )
                    num_splits += 1
                else:
                    if (stream_loc not in next_stream_locs):
                        next_stream_locs.append( stream_loc )
            #logging.debug(f"streams at {next_stream_locs}")
            cur_stream_locs = next_stream_locs
        return( num_splits )
    
    
    # This needs to be depth first to make the patterns usable
    def depth_search( self, row_index, stream_loc ):
        our_search_id=f"R{row_index}S{stream_loc}"
        if (our_search_id in self.done_searches):
            # we've passed this way before
            # logging.debug("Cache hit at {our_search_id}")
            return( self.done_searches[our_search_id])
        new_time_lines=0
        if (row_index >= self.num_splitter_rows-1):
            return 0
        logging.debug(f"Checking stream at row {row_index} col {stream_loc}")
        self.counter=0
        if (self.splitter_matrix[row_index][stream_loc] == "^"):
            # logging.debug(f"Split at row {row_index} col {stream_loc}")
            new_time_lines += self.depth_search( row_index+1, stream_loc-1 )
            new_time_lines += self.depth_search( row_index+1, stream_loc+1 )
            new_time_lines += 1
        else:
            new_time_lines += self.depth_search( row_index+1, stream_loc )
        # logging.debug(f"Adding R{row_index}S{stream_loc} = {new_time_lines}")
        self.done_searches[ our_search_id ] = new_time_lines
        return( new_time_lines )
        
    
    def total_part2( self ):
        # Count timelines + the original
        timelines=self.depth_search( 0, self.splitter_line.index('S') )+1
        return( timelines )
            
def read_input( inputStream, part):
    matrix=[]
    for line in inputStream:
        chars=list(line.rstrip("\n"))
        matrix.append( chars )

    problems=TacyonClass( matrix )
    if (part == 1):
        return( problems.total_part1() )
    else:
        return( problems.total_part2( ) )

# main
if __name__ == '__main__':
    # logging.basicConfig(level=getattr(logging, "DEBUG"))
    print(f"Total splits are {read_input( sys.stdin, 2 )}")

