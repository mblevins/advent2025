# !/bin/python3
# https://adventofcode.com/2025/day/7

import sys
import logging
import re
import copy

class PanelLine:

    #  lights= ".##."
    #  buttons=["(3)","(1,3)","(2)","(2,3)","(0,2)","(0,1)"]
    #  jolts=[3,5,4,7]
    def __init__( self, lights, buttons, jolts ):
        self.needed_light_state=list(lights)
        self.buttons=[]
        for b in buttons:
            self.buttons.append([int(s) for s in b[1:len(b)-1].split(",")])
        self.jolts=jolts

    # press all tthe buttons specified by the press list
    # don't worry about early successes, as we'ved tried 
    # this in order of successively increasing numbers
    def make_attempt( self, push_list ):
        light_state = ["."] * len( self.needed_light_state )
        for p in push_list:
            button=self.buttons[p]
            for li in button:
                if (light_state[li] == '.'):
                    light_state[li] = '#'
                else:
                    light_state[li] = '.'
        return( light_state == self.needed_light_state )
    
    # returns a list of lists
    def all_combos_for_n( self, num_pushes ):

        num_buttons=len( self.buttons )
        pushes=[-1]*num_pushes
        combos=[]
        for r in range( 0, num_buttons**num_pushes):
            for c in range( 0, num_pushes):
                if ((r % num_buttons**c) == 0):
                    pushes[c] = pushes[c] + 1
                    if pushes[c] == num_buttons:
                        pushes[c] = 0
            combos.append( copy.copy( pushes ) )

        return( combos  )
        
    # pass 1
    def try_combos( self ):

        # max presses is kinda arbitrary, but we're probably going to run out of memory at some point
        max_presses=10
        success=False
        
        for num_presses in range( 0, max_presses ):
            combos=self.all_combos_for_n( num_presses)
            for co in combos:
                if (self.make_attempt( co )):
                    logging.debug(f"Success on combo {co}") 
                    success=True
                    break
            if (success):
                break


        if (not success):
            raise Exception("Didn't find any success combos")
        
        return( num_presses )

def read_input( inputStream, part):

    panel_lines=[]
    for line in inputStream:
        # [.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
        linematch=re.match(r"^\[([.#]+)\] ([(\d, )]+) \{([\d,]+)\}", line)
        if not linematch:
            raise Exception("Unrecognized line:" + line )
        panel_lines.append( PanelLine( linematch.group(1), linematch.group(2).split(), linematch.group(3) ))

    sum=0
    if (part == 1):
        for p in panel_lines:
            sum += p.try_combos()
    return( sum )

# main
if __name__ == '__main__':
    logging.basicConfig(level=getattr(logging, "DEBUG"))
    print(f"Sum is {read_input( sys.stdin, 1)}")

