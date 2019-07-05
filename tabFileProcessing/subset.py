#!/usr/bin/env python

'''
1. fname to subset from
2. fname with keys to extract
3. colnumber in file1
4. colnumber in file2
5. getDiff? (y/n) (return subset by default, if yes, return all in f1 that are not in f2)

'''

import sys
from collections import defaultdict

try:
    f1name = sys.argv[1]
    f2name = sys.argv[2]
    col1   = int(sys.argv[3]) - 1
    col2   = int(sys.argv[4]) - 1
except:
    exit(__doc__)

if len(sys.argv) > 5:
    diff = sys.argv[5]
else:
    diff = 'n'

d = defaultdict(list)
f = open(f1name, 'r')
for l in f:
    segs = l.rstrip().split('\t')
    try:
        key = segs[col1]
    except:
        print("this row does not have the column you are looking for")
        exit(segs)
    d[key].append(l)
f.close()

keys = defaultdict(str)
f = open(f2name, 'r')
for l in f:
    segs = l.rstrip().split('\t')
    key = segs[col2]
    keys[key] = 1
f.close()


for key1 in d:
    if diff.lower() == 'y':
        if not key1 in keys:
            rows = d[key1]
            for r in rows:
                print(r.rstrip())
    elif diff.lower() == 'n':
        if key1 in keys:
            rows = d[key1]
            for r in rows:
                print(r.rstrip())
    else:
        exit(__doc__)


