#!/usr/bin/env python
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    line = line.strip()
    # split the line into words
    tab = line.split("\t")
    user = int(tab[0])
    if len(tab)>1:
        frnds  = tab[1]
        if frnds != '':
            friends = map(int, frnds.split(","))
            for i in range(len(friends)):
                f1 = friends[i]
                s1 = ""
                if (user <= f1):
                    s1 = str(user) + " " + str(f1)
                    print '%s,%s\t0' % (s1, 0)
                else:
                    s1 = str(f1) + " " + str(user)
                    print '%s,%s\t0' % (s1, 0)
                j = i +1
                while j < len(friends):
                    f2 = friends[j]
                    if f1 < f2:
                        s2 = str(f1)+" " + str(f2)
                        print '%s,%s\t0' % (s2, 1)
                    else:
                        s2 = str(f2)+" " + str(f1)
                        print '%s,%s\t0' % (s2, 1)
                    
                    j = j+1
