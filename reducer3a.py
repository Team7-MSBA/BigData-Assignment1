#!/usr/bin/env python

from operator import itemgetter
import sys

#'s2,0\t0'
#'1 2,0\t0'
#'1 2,1\t0'

numMutualFriends = 0
current_pair = None
current_count = 0
badfactor = None
pair = None

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    line2 = line.split('\t')
    line3 = line2[0]
    line4 = line3.split(',')
    pair = line4[0]
    count = line4[1]

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue
    #print pair,"----", current_pair,"----",count,"----",current_count
    if pair != current_pair:
        if current_pair != None and current_count !=0:
            print '%s\t%s' %(current_pair,current_count)
            current_count = 0
        if count == 0:
            badfactor = 1
            current_pair = pair
            continue
        else:
            current_pair = pair
            current_count = count
            badfactor = 0

    else:
        #print badfactor
        if badfactor != 1:
            current_count = current_count + count
        else:
            continue
