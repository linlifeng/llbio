#!/usr/bin/python

'''
1. blo m8 format output 
2. query file length
3. allowed mismatch
'''
from sys import argv
from collections import defaultdict

try:
    blom8f    = open(argv[1])
    lenf      = open(argv[2])
    allowedMM = int(argv[3])
except:
    exit(__doc__)


lenD = defaultdict(int)
for l in lenf:
    segs = l.rstrip().split('\t')
    seqName, seqLen = segs[:2]
    lenD[seqName] = int(seqLen)
lenf.close()    


for l in blom8f:
    '''
    segs[0]	col_1	KRAS_p.G12A_c.35G>C_mut
    segs[1]	col_2	NC_000020.11
    segs[2]	col_3	100.000
    segs[3]	col_4	14
    segs[4]	col_5	0
    segs[5]	col_6	0
    segs[6]	col_7	1
    segs[7]	col_8	14
    segs[8]	col_9	47942880
    segs[9]	col_10	47942867
    segs[10]	col_11	101
    segs[11]	col_12	26.5
    '''
    segs = l.rstrip().split('\t')
    q, h, perc, M, m, g, qs, qe, s, e, evalue, score = segs
    hitCoord = '|'.join([h, s, e])
    qlen = lenD[q]
    match = int(M) - int(m) - int(g)
    mm = qlen - match
    if mm <= allowedMM:
        print l.rstrip() 

blom8f.close()

