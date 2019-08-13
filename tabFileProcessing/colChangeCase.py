#!/usr/bin/python
'''
1. file name
2. colnumber
3. case to be changed to (upper/lower)
'''

from sys import argv, exit

try:
    f      = open(argv[1], 'r')
    colnum = int(argv[2]) - 1
    case   = argv[3]
except:
    exit(__doc__)

for l in f:
    segs = l.rstrip().split('\t')
    colContent = segs[colnum]
    if case == 'upper':
        newContent = colContent.upper()
    elif case == 'lower':
        newContent = colContent.lower()
    else:
        exit("ERROR: unrecognized case %s. Should be upper or lower"%case)
    print "\t".join(segs[:colnum] + [newContent] + segs[colnum+1:])
