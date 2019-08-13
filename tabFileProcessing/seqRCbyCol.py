#!/usr/bin/python
'''
1. tab file
2. column to RC
'''

from sys import argv, exit

try:
    f   = open(argv[1], 'r')
    col = int(argv[2]) - 1
except:
    exit(__doc__)

def string_rc(s):
    comp = { \
        'A': 'T', \
        'T': 'A', \
        'C': 'G', \
        'G': 'C', \
        'a': 't', \
        't': 'a', \
        'c': 'g', \
        'g': 'c'
    }
    comps = []
    for l in s:
        if not l in comp:
            return "ERROR: unrecognized base: %s"%l
        comps.append(comp[l])
    comps.reverse()
    return ''.join(comps)

for l in f:
    segs   = l.rstrip().split("\t")
    seq    = segs[col]
    seq_rc = string_rc(seq)
    print l.rstrip() + '\t' + seq_rc 

