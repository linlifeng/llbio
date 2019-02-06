#!/usr/bin/env python

'''
1. file name
2. column to add
3. prefix 
4. suffix? (y/n)
'''

from sys import argv, exit
import Bio
from os import system

try:
    fname = argv[1]
    col = int(argv[2]) - 1
    prefix = argv[3]
    isSuffix = argv[4]
except:
    exit(__doc__)

f = open(fname, 'r')

for l in f:
    segs = l.rstrip().split('\t')
    if isSuffix.upper() == 'Y':
        segs[col] = segs[col] + prefix
    else:
        segs[col] = prefix + segs[col]
    print('\t'.join(segs))


f.close()
