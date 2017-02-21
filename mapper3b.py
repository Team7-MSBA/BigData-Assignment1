#!/usr/bin/env python
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    # split the line into words
    tab = line.split("\t")
    friends = tab[0].split(" ")
    f1 = int(friends[0])
    f2 = int(friends[1])
    numMutual = int(tab[1])
    print '%s\t%s,%s' %(f1,f2,numMutual)
    print '%s\t%s,%s' %(f2,f1,numMutual)
