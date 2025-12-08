# !/bin/python3
# https://adventofcode.com/2025/day/7

import sys
import logging
import numpy as np


class JunctionPairClass:

    def __init__( self, j1, j2, distance ):
        self.j1 = j1
        self.j2 = j2
        self.distance = distance

class  CircuitClass:

    def __init__( self, id ):
        self.id = id
        self.connections=[]

    def add( self, id ):
        self.connections.append( id )

    def extend_list( self, id_list ):
        self.connections.extend( id_list )

    def is_in_circuit( self, id ):
        if id in self.connections:
            return( True )
        return( False )
        

class JunctionClass:

    def __init__( self, matrix  ):
        self.junction_loc_array = np.array( matrix, dtype=int)

    # helper method
    def get_id( self, row_index ):
        return( f"{"/".join([str(x) for x in self.junction_loc_array[row_index]])}" )
    
    # return a circuit id or None
    def find_matching_circuit( self, circuit_dict, id ):
        for c_id in circuit_dict:
            circuit=circuit_dict[c_id]
            if circuit.is_in_circuit( id ):
                return( circuit )
        return( None )

    # part 1 total
    def total_part_1( self, max_conn ):

        # build a list of pairs, indexed by pair id
        junction_pair_dict={}
        for r1_i in range( 0, len( self.junction_loc_array )):
            for r2_i in range( 0, len( self.junction_loc_array )):
                if (r1_i == r2_i):
                    continue
                r1_id = self.get_id( r1_i )
                r2_id = self.get_id( r2_i )
                pair_id = f"{r1_id}:{r2_id}"
                reverse_id = f"{r2_id}:{r1_id}"
                if reverse_id in junction_pair_dict:
                    # already did this one the other direction
                    continue
                distance=round(np.linalg.norm(self.junction_loc_array[r1_i] - self.junction_loc_array[r2_i]))
                junction_pair_dict[pair_id]=JunctionPairClass( r1_id, r2_id, distance )

        # Now sort the dict by distance, we can toss the index now
        junction_pairs = sorted(list(junction_pair_dict.values()), key=lambda item: item.distance)
        junction_pair_dict=None

        # Now walk through the sorted distances and match up circuits
        num_circuits=0

        # list of CircuitClass 
        circuit_dict={}
        conn_count=0
        for jp in junction_pairs:

            conn_count += 1
            if (conn_count > max_conn):
                break


            c1 = self.find_matching_circuit( circuit_dict, jp.j1 )
            c2 = self.find_matching_circuit( circuit_dict, jp.j2 )

            logging.debug(f"jp.j1={jp.j1}, jp.j2={jp.j2}")

            if (c1 and c1 == c2):
                # counts as a connection, but nothing to do
                logging.debug(f" ... circuits {c1.id} and {c2.id} already in same circuit")
            elif (c1):
                if (c2):
                    logging.debug(f" ... extending circuit {c1.id} with circuit {c2.id}")
                    c1.extend_list(c2.connections)
                    del circuit_dict[c2.id]
                else:
                    logging.debug(f" ... adding j2 to circuit {c1.id}")
                    c1.add(jp.j2)
            elif (c2):
                # if we're here, c1 must be None
                logging.debug(f" ... adding j1 to circuit {c2.id}")
                c2.add(jp.j1)
            else:
                # neither c1 nor c2 are in curcuits, create a new circuit
                circuit_id=f"C{num_circuits}"
                logging.debug(f" ... Creating new circuit {circuit_id}")
                circuit=CircuitClass( circuit_id )
                circuit.add( jp.j1 )
                circuit.add( jp.j2 )
                circuit_dict[ circuit_id ] = circuit
                num_circuits += 1
        
        # now sort the circuit dict and toss it, we just need the array
        circuits = sorted(list(circuit_dict.values()), key=lambda item: len( item.connections ), reverse=True)
        for top in range( 0, 3 ):
            circuit=circuits[top]
            logging.debug(f"circuit {circuit.id}: {len( circuit.connections )} : {",".join( circuit.connections)}")
        circuit_dict=None

        # total and goodnight
        total = len( circuits[0].connections ) * len( circuits[1].connections ) * len( circuits[2].connections )
        return( total )
    

def read_input( inputStream, part, max_conn):
    matrix=[]
    for line in inputStream:
        coord_str=line.split(",")
        matrix.append( coord_str )

    junctions=JunctionClass( matrix )
    if (part == 1):
        return( junctions.total_part_1( max_conn ) )
    else:
        return( junctions.total_part2( max_conn  ) )

# main
if __name__ == '__main__':
    # logging.basicConfig(level=getattr(logging, "DEBUG"))
    print(f"Total splits are {read_input( sys.stdin, 1, 1000)}")

