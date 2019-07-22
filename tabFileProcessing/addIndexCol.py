#!/usr/bin/env python
'''
add an index column to the very beginning of the file.

1. file name
2. start from number (will be the first number, the rest will autoincrement)
'''

from sys import argv
try:
    f        = open(argv[1], 'r')
    startNum = int(argv[2])
except:
    exit(__doc__)

i = startNum
for l in f:
    segs = l.rstrip().split('\t')
    segs[0] = str(i)
    print '\t'.join(segs)
    i += 1
f.close()
