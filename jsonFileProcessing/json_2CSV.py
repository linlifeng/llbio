#!/usr/bin/env python
'''
1. json file, one line per object
'''

from sys import argv, exit

import pandas
import json
import csv

try:
    fname = argv[1]
except:
    exit(__doc__)

f = open(fname, 'r')
#df = pandas.read_json(f)
#print df
for l in f:
    #print l
    json_parsed = pandas.read_json(l)
    json_csv = json_parsed.to_csv(sep='\t')
    print json_csv
    #print json_parsed

f.close()
