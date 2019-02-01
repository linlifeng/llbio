#!/usr/bin/env python

'''

1. file name
2. into how many files?

'''

from sys import argv, exit
import Bio
from os import system

try:
    fname = argv[1]
    fnumber = int(argv[2])
except:
    exit(__doc__)

f = open(fname, 'r')

i = 0
files = {}
for l in f:
    bucket = i % fnumber + 1
    if bucket in files:
        files[bucket].append(l)
    else:
        files[bucket] = [l]
    i += 1

f.close()

for bucket in files:
    of = open('%s_%s'%(fname, bucket), 'w')
    for l in files[bucket]:
        of.write(l)
    of.close()
