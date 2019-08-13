#!/usr/bin/env python
'''
1. tab file containing json column.
2. json column in file
'''

from sys import argv, exit
from collections import defaultdict

import json
import csv

try:
    fname = argv[1]
    col   = int(argv[2]) - 1
except:
    exit(__doc__)

f = open(fname, 'r')
contentDict = defaultdict(lambda: defaultdict(list))
uniqKeys = []
i = 0
for l in f:
    jsonString = l.rstrip().split('\t')[col]
    jsonDict   = json.loads(jsonString)
    for key in jsonDict:
        contentDict[i][key] = jsonDict[key]
        uniqKeys.append(key) # this is not unique yet.
    i += 1
f.close()

uniqKeys = set(uniqKeys)
print('\t'.join(uniqKeys))
for i in contentDict:
    #print(i, contentDict[i])
    fields = contentDict[i]
    row = ''
    for key in uniqKeys:
        row += (str(fields[key]) + '\t')
    print(row.replace('\t$',''))