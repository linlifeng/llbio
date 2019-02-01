#!/usr/bin/env python

'''
1. fasta file

output a bed file with all the non-ATCG bases and their positions.
'''

from sys import argv, exit
from Bio import SeqIO
from os import system

try:
    fname = argv[1]
except:
    exit(__doc__)

f = open(fname, 'r')
records = SeqIO.parse(f, 'fasta')

for record in records:
    seqName = record.description
    seqShortName = record.id
    sequence = record.seq
    i = 0
    for base in sequence:
        i += 1
        if base.upper() not in ['A', 'T', 'C', 'G']:
            print "%s\t%s\t%s\t%s"%(seqShortName, i - 1, i, base)
