#!/usr/bin/env python

'''
1. tab file 2 columns
'''
from sys import argv

try:
    f = open(argv[1])
except:
    exit(__doc__)


for l in f:
    name, seq = l.rstrip().split('\t')[:2]
    print(">" + name + "\n"  + seq)
