#!/usr/bin/env python

'''
1. fname
2. json col number
3. key to extract
4. key value to subset
'''

import sys, pprint
import json
from collections import defaultdict
pp = pprint.PrettyPrinter(indent=4)

try:
    fname = sys.argv[1]
    col = int(sys.argv[2]) - 1
    queryKey = sys.argv[3]
    queryValue = sys.argv[4]
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


            ## to print out one of the json values by key
            #if jsonkey == queryKey:
            #    content = jsoncontent[jsonkey]
                #pieces = content.split('[')

            #    ttype.append(content)

            # to further separate each subtypes
            if jsonkey == queryKey and jsoncontent[jsonkey] == queryValue:
                ttype.append(l.rstrip())



            #ttype.append(jsonkey)
            '''
            value = jsoncontent[jsonkey]
            stillJson = False
            try:
                #json.loads(value)
                stillJson = True
            except:
                pass
            if stillJson:
                jsonKey += '_stillJson'
            '''
    except:
        continue
    keys.append(key)

for key in keys:
    key.sort()
    #print(key)

for t in ttype:
    print t
    pass

#for q in qualities:
#    print("%s\t%s"%(q, len(qualities[q])))

#print(set(combinedKeys))
