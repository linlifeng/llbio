#!/usr/bin/python

'''
1. bed file
2. linear genome size

this simply split any bed region (such as an amplicon) that span across the start and end of the circular chromosome to be mapped to end and beginning separately.
Sometimes during the design, the end of the linearized circular sequences is artificially extended to mimic the junction in a linear manner.
This will ensure full coverage of the sequence, but will need to restore to the original coordinates for mapping

'''

from sys import argv, exit


try:
    fname = argv[1]
    gsize = int(argv[2])
except:
    exit(__doc__)

f = open(fname, 'r')

for l in f:
    segs = l.rstrip().split('\t')
    if 'track' == l[:5]:
        print l.rstrip()
        continue
    chrm, start, end = segs[:3]
    soverhang = int(start) + 1 - gsize #bed file is 0-based, so need to add 1 to calculate.
    eoverhang = int(end) - gsize
    if soverhang > 0:
        print '\t'.join([chrm, str(soverhang - 1), str(eoverhang)] + segs[3:])
    elif eoverhang > 0:
        print '\t'.join([chrm, start, str(gsize)] + segs[3:])
        print '\t'.join([chrm, '0', str(eoverhang)] + segs[3:])
    else:
        print '\t'.join(segs)
        
