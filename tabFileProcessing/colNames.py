#!/usr/bin/env python

import sys

for line in sys.stdin:
    segs = line.rstrip().split('\t')
    for i in range(len(segs)):
        print("segs[{}]\tcol_{}\t{}".format(i, i+1, segs[i]))
    break
