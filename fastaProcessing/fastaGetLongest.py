#!/usr/bin/python

'''
1. fastaFile
'''

from sys import argv, exit
from Bio import SeqIO
from os import path, system

try:
    fname = argv[1]
except:
    exit(__doc__)


longest = [None, None, None]
f = open(fname, 'r')
records = SeqIO.parse(f, 'fasta')
for r in records:
    name = r.id
    sequence = r.seq
    if len(sequence) > longest[2]:
        longest = [name, sequence, len(sequence)]

f.close()

print ">%s\n%s"%(longest[0], longest[1])

