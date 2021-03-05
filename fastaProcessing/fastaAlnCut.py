#!/usr/bin/env python

'''
1. fasta file (assume already aligned)
2. start (1-based)
3. end

'''

from sys import argv, exit
from Bio import SeqIO
from os import system

try:
    fname = argv[1]
    start = int(argv[2])
    end = int(argv[3])
except:
    exit(__doc__)

f = open(fname, 'r')
records = SeqIO.parse(f, 'fasta')

for record in records:
    seqName = record.description
    seqShortName = record.id
    sequence = record.seq
    frag = sequence[start-1:end]
    print("%s_%s_%s\t%s"%(seqName, start, end, frag))

f.close()
