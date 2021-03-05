#!/usr/bin/env python

'''
split a column and append to the end of the table.
1. fname
2. col number 
3. delimiter
'''

import sys
from collections import defaultdict

try:
    fname = sys.argv[1]
    col = int(sys.argv[2]) - 1
    delimiter = sys.argv[3]
except:
    exit(__doc__)

f = open(fname, 'r')
for l in f:
    segs = l.rstrip().split("\t")
    col_content = segs[col]
    splitted = col_content.split(delimiter)
    print("\t".join(segs + splitted))
