# !/bin/python3
# https://adventofcode.com/2025/day/7

import sys
import logging

        
class TileClass:

    def __init__( self, matrix  ):
        # creat
        self.red_tiles=[]
        self.max_x=0
        self.max_y=0
        for row in matrix:
            self.red_tiles.append( (row[0], row[1]) )
            if (row[0] > self.max_y):
                self.max_y = row[0]
            if (row[1] > self.max_x):
                self.max_x = row[0]
    
    def do_area( self, c1, c2 ):
        area=(abs( c1[0]-c2[0] )+1) * (abs( c1[1]-c2[1] )+1)
        logging.debug( f"Area of {c1[0]}/{c1[1]} and {c2[0]}/{c2[1]} is {area}")
        return( area )

    def total_part_1( self ):

        # Find the outermost corners
        # kinda stupid to do it this way, but there are only four corners
        # keep a list in vase of ties, we want them both
        ul_dist=self.max_x + self.max_y
        ul_coord=None
        ur_dist=self.max_x + self.max_y
        ur_coord=None
        ll_dist=self.max_x + self.max_y
        ll_coord=None
        lr_dist=self.max_x + self.max_y
        lr_coord=None
        for coord in self.red_tiles:
            # upper left
            candidate_dist = coord[0] + coord[1]
            if (candidate_dist <= ul_dist):
                logging.debug(f"New UL candidate: {coord[0]}/{coord[1]}={candidate_dist} ")
                ul_dist = candidate_dist
                ul_coord = coord

            # upper right
            candidate_dist = self.max_y - coord[0] + coord[1]
            if (candidate_dist == ul_dist or candidate_dist == ur_dist or candidate_dist == ll_dist or candidate_dist == lr_dist):
                raise Exception("Hit a dup, this may throw things off")
            if (candidate_dist < ur_dist):
                logging.debug(f"New UR candidate: {coord[0]}/{coord[1]}={candidate_dist} ")
                ur_dist = candidate_dist
                ur_coord = coord
            #  lower left
            candidate_dist = coord[0] + self.max_x - coord[1]
            if (candidate_dist <= ll_dist):
                logging.debug(f"New LL candidate: {coord[0]}/{coord[1]}={candidate_dist} ")
                ll_dist = candidate_dist
                ll_coord = coord
            #  lower right
            candidate_dist = self.max_y - coord[0] + self.max_x - coord[1]
            if (candidate_dist <= lr_dist):
                logging.debug(f"New LR candidate: {coord[0]}/{coord[1]}={candidate_dist} ")
                lr_dist = candidate_dist
                lr_coord = coord

    
        all_corners = [ ul_coord, ur_coord, ll_coord, lr_coord ]
        areas=[]
        for a in all_corners:
            for b in all_corners:
                if (a is not b):
                    areas.append( self.do_area( a, b) )
        return( int(sorted( areas, reverse=True )[0]) )
    

def read_input( inputStream, part):
    matrix=[]
    for line in inputStream:
        coords=[int(s) for s in line.strip().split(",")]
        matrix.append( coords )

    tiles=TileClass( matrix )
    if (part == 1):
        return( tiles.total_part_1(  ) )
    else:
        return( tiles.total_part_1(  ) )

# main
if __name__ == '__main__':
    logging.basicConfig(level=getattr(logging, "DEBUG"))
    print(f"Sum is {read_input( sys.stdin, 1)}")

