#!/usr/bin/env python

'''
1. fasta file
2. min primer len
3. max primer len
4. step
'''

from sys import argv, exit
from Bio import SeqIO
from os import system

try:
    fname = argv[1]
    minLen = int(argv[2])
    maxLen = int(argv[3])
    step = int(argv[4])
except:
    exit(__doc__)


def genFrag(name, seq, length, step):
    i = 0
    while i + length <= len(seq):
        start = i
        end = i + length
        print ">%s_%s-%s"%(name, start+1, end)
        print seq[start: end]
        i += step

f = open(fname, 'r')
records = SeqIO.parse(f, 'fasta')
for r in records:
    name = r.id
    sequence = r.seq
    for l in range(minLen, maxLen + 1):
        genFrag(name, sequence, l, step)

f.close()
