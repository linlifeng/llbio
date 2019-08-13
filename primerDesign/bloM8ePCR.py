#!/usr/bin/python

'''
1. blo m8 format output 
version 0.1
dumb matching of close together paired matches from opposite strands

TODO:
check if matching extensible
check number of mismatches
check Tm?
'''
from sys import argv
from collections import defaultdict

try:
    blom8f = open(argv[1])
    #maxLen = int(argv[2])
except:
    exit(__doc__)


bindingSites = defaultdict(list)
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
    '''
    if int(s) > int(e):
        strand  = '-'
    else:
        strand  = '+'
    '''
    bindingSites[hitCoord].append(q)
blom8f.close()

for site in bindingSites:
    for site2 in bindingSites:
        chr1, s1, e1 = site.split('|')
        chr2, s2, e2 = site2.split('|')
        s1, e1 = int(s1), int(e1)
        s2, e2 = int(s2), int(e2)
        strand1 = '+'
        strand2 = '+'
        if s1 > e1:
            strand1 = '-'
        if s2 > e2:
            strand2 = '-'
        p1List = bindingSites[site]
        p2List = bindingSites[site2]

        #print p1List
        if not chr1 == chr2:
            continue
        if strand1 == strand2:
            continue
            print strand1        
        #'''
        if strand1 == '+' and s1 > s2:
            continue
        if strand2 == '+' and s2 > s1:
            continue
        #'''
        
        ampLen = max(s1,s2,e1,e2) - min(s1,s2,e1,e2) + 1

        if strand1 == '+':
            print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s"%(chr1, s1, e1, e2, s2, ampLen, p1List, p2List)
        if strand2 == '+':
            print "%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s"%(chr1, s2, e2, e1, s1, ampLen, p1List, p2List)
