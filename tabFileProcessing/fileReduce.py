#!/usr/bin/env python

'''
print out every Nth row of a file.
a non-random subsampling.

1. file name
2. N
'''

from sys import argv, exit
import Bio
from os import system

try:
    fname = argv[1]
    N = int(argv[2])
except:
    exit(__doc__)

f = open(fname, 'r')

i = 0 
for l in f:
    i += 1
    #segs = l.rstrip().split('\t')
    if i % N == 1:
        print(l.rstrip())

f.close()
