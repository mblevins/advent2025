# !/bin/python3
# https://adventofcode.com/2025/day/2

import re
import sys
import logging

class JoltClass:
    
    def __init__( self ):
        self.invalid_ids = {}
    
    def find_largest_2( self, bank_str ):
        if len( bank_str ) < 2:
            raise Exception("Bank isn't large enough")
        # convert the string to an array of intergers, easier that way
        bank=[]
        for i in range( 0, len( bank_str )):
            bank.append( int( bank_str[i]))

        # make a a multi pass scan, 1st for to find the largest
        # number(s), and 2nd for second highest,
        # if two numbers are the same, take the first
        # skip the last number for the large check
        h1_value=0
        h1_index=0
        for i in range( 0, len( bank )-1 ):
            if (bank[i] > h1_value):
                h1_value = bank[i]
                h1_index=i
        h2_value=0
        for i in range( h1_index+1, len( bank )):
            if (bank[i] > h2_value):
                h2_value=bank[i]
        logging.debug(f"bank_str={bank_str}, h1_value={h1_value}, h1_index={h1_index}, h2_value={h2_value}")
        return( h1_value * 10 + h2_value )
    
    def find_largest_N( self, bank_str, max_match ):
        if len( bank_str ) < max_match:
            raise Exception("Bank isn't large enough")
        # convert the string to an array of intergers, easier that way
        bank=[]
        for i in range( 0, len( bank_str )):
            bank.append( int( bank_str[i]))

        # make a multi pass scan, 1st for to find the largest
        # number(s), and 2nd for second highest
        # if two numbers are the same, take the first
        # skip the last numbers
        h_values=[]
        last_high_index=-1
        for n in range( 0, max_match ):
            current_high=0
            for i in range( last_high_index+1, len( bank )-max_match + n + 1 ):
                if (bank[i] > current_high):
                    current_high=bank[i]
                    last_high_index=i
            h_values.append( current_high )

        sum=0
        for i in range(0, max_match-1):
            sum += h_values[i]
            sum = sum * 10
        sum += h_values[max_match-1]

        logging.debug(f"bank_str={bank_str}, sum={sum}")
        return( sum )

def read_input( inputStream ):
    jolt=JoltClass()
    sum=0
    for line in inputStream:
        line=line.strip()
        if (len(line) == 0):
            continue

        logging.debug(f"line={line}")
        sum += jolt.find_largest_2( line )

    return( sum )

# main
if __name__ == '__main__':
    print(f"The largest battery combo is {read_input( sys.stdin )}")

