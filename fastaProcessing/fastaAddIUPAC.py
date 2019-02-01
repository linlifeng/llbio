#!/usr/bin/env python

'''
1. fasta file
2. conversion file: format:
chrM    210     A       R
chrM    16184   C       Y
chrM    663     A       R
chrM    9477    G       R
chrM    15326   A       R
chrM    13368   G       R
chrM    16274   G       R
chrM    6962    G       R
chrM    499     G       R

'''

from sys import argv, exit
from Bio import SeqIO
from os import system

try:
    fname = argv[1]
    cfname = argv[2]
except:
    exit(__doc__)

f = open(cfname, 'r')
translate = {}
for l in f:
    segs = l.rstrip().split('\t')
    chrm, pos, curr, deg = segs[:4]
    if chrm + '_' + pos in translate:
        exit("non-unique positions found: %s"%(chrm + "_" + pos))
    translate[chrm + "_" + pos] = [curr, deg]
f.close()

f = open(fname, 'r')
records = SeqIO.parse(f, 'fasta')
for record in records:
    seqName = record.description
    seqShortName = record.id
    sequence = record.seq
    baseList = list(sequence)
    for i in range(len(baseList)):
        key = seqShortName + '_' + str(i + 1)
        if key in translate:
            if translate[key][0] == baseList[i]:
                baseList[i] = translate[key][1]
            else:
                exit("reference base does not match: %s, %s"%(baseList[i], translate[key][0]))
    print ">%s\n%s"%(seqName, ''.join(baseList))
f.close()
