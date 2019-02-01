#!/usr/bin/env python

'''
1. fasta file
2. tag sequence
3. prefix / suffix

'''

from sys import argv, exit
from Bio import SeqIO
from os import system

try:
    fname = argv[1]
    tseq = argv[2]
    position = argv[3]
except:
    exit(__doc__)
if not position in ['prefix', 'suffix']:
    exit("the third argument should be either 'prefix' or 'suffix'")


f = open(fname, 'r')
records = SeqIO.parse(f, 'fasta')

for record in records:
    seqName = record.description
    seqShortName = record.id
    sequence = record.seq
    if position == 'prefix':
        newSeq = tseq + sequence
    else:
        newSeq = sequence + tseq
    print ">%s_tagged\n%s"%(seqShortName, newSeq)

f.close()
