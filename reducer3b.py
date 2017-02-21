#!/usr/bin/env python

from operator import itemgetter
import sys

current_user = None
current_friends = None
current_mutuals = [0,0,0,0,0,0,0,0,0,0]
counta = 0
for line in sys.stdin:
    line = line.strip()
    tab = line.split("\t")
    user = int(tab[0])
    dal = tab[1].split(",")
    friend = int(dal[0])
    numMutual = int(dal[1])
    counta = counta + 1

    #print user,'----',current_user,'----',numMutual,"----",(friends)," ----"
    if user != current_user:
        if current_user != None:
            current_friends = filter(lambda a: a !=.001, current_friends)
            print '%s::    %s' %(current_user,str(current_friends).strip('[]'))
            current_user = user
            current_friends = [friend,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001]
            current_mutuals = [numMutual,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001]
        else:
            current_user = user
            current_friends = [friend,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001]
            current_mutuals = [numMutual,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001,0.001]
    else:
        if numMutual>min(current_mutuals):
            current_friends[current_mutuals.index(min(current_mutuals))] = friend
            current_mutuals[current_mutuals.index(min(current_mutuals))] = numMutual

