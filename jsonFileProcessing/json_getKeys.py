#!/usr/bin/env python


#!/usr/bin/env python

'''
1. fname
2. json col number
'''

import sys, pprint
import json
from collections import defaultdict

try:
    fname = sys.argv[1]
    col = int(sys.argv[2]) - 1
except:
    exit(__doc__)

f = open(fname, 'r')
keys = []
combinedKeys = []
ttype = []
qualities = defaultdict(list)

for l in f:
    segs = l.rstrip().split('\t')
    s = segs[col]
    key=[]
    try:
        jsoncontent = json.loads(s)
        for jsonkey in jsoncontent:
            key.append(jsonkey)
            combinedKeys.append(jsonkey)
            qualities[jsonkey].append(jsoncontent[jsonkey])
    except:
        key.append("error " + s )
    keys.append(key)

for key in keys:
    key.sort()
    print(key)

