#!/usr/bin/env python

'''
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
    print("%s\t%s\t%s"%(seqShortName, len(sequence), seqName))
