#!/usr/bin/env python

'''
split the file into subfiles based on the unique values of a column
1. fname
2. col to use for spliting
'''

import sys
from collections import defaultdict

try:
    fname = sys.argv[1]
    col = int(sys.argv[2]) - 1
except:
    exit(__doc__)

f = open(fname, 'r')
d = defaultdict(list)
for l in f:
    segs = l.rstrip().split('\t')
    for i in range(len(segs)):
        if i == col:
            key = segs[i]
            d[key].append(l)        
        i += 1
size = len(d)
if size > 1000:
    exit("[ERROR]Maximum allowed subfiles is 1000. Currently you are creating %s files"%size)

for key in d:
    f = open(fname+key,'w')
    for l in d[key]:
        f.write(l)
    f.close()
