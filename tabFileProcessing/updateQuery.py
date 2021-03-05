#!/usr/bin/env python

'''
1. fname to append column to
2. fname to get info from
3. col in first file to match
4. col in second file to match
5. col in second file to append (use all to add everything)
'''

import sys
from collections import defaultdict

try:
    f1name = sys.argv[1]
    f2name = sys.argv[2]
    col1 = int(sys.argv[3]) - 1
    col2 = int(sys.argv[4]) - 1
    colToAppend_0 = sys.argv[5]
except:
    exit(__doc__)


f = open(f2name, 'r')
d = defaultdict(list)
for l in f:
    segs = l.split('\t')
    key = segs[col2].rstrip()
    if colToAppend_0.lower() == 'all':
        d[key].append(l.rstrip())
    else:
        try:
            colToAppend = int(colToAppend_0) - 1
        except:
            exit(__doc__)
        d[key].append(segs[colToAppend])
f.close()

f = open(f1name, 'r')
for l in f:
    segs = l.split('\t')
    key1 = segs[col1].rstrip()
    if key1 in d:
        toAppend = d[key1]
    else:
        toAppend = ['NULL']
    for hit in toAppend:
        print(l.rstrip() + '\t' + hit.rstrip())
f.close()