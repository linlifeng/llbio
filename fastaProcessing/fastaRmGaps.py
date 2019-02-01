#!/usr/bin/env python

'''
1. fasta file
2. gap notation (e.g. '-')

print on screen
'''

from sys import argv, exit
from Bio import SeqIO
from os import system

try:
    fname = argv[1]
    gapSymbol = argv[2]
except:
    exit(__doc__)

f = open(fname, 'r')
records = SeqIO.parse(f, 'fasta')

for record in records:
    seqName = record.description
    seqShortName = record.id
    sequence = record.seq
    ungapped = str(sequence).replace(gapSymbol, '')
    print ">%s\n%s"%(seqName, ungapped)

f.close()
