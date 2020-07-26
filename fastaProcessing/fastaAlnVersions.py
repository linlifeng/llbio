#!/usr/bin/python

'''
for a fasta alignment, craete a lookup file with seqName and v number
this is useful for window scanning analysis, mapping back the primer versions to their origins.

input

1. fasta alignment file

'''

from sys import argv, exit
from Bio import SeqIO

try:
    fname = argv[1]
    f = open(fname, 'r')
except:
    exit(__doc__)

records = SeqIO.parse(f, 'fasta')

i = 1
for r in records:
    print "%s\t%s\tv%s"%(r.id, r.description, i)
    i += 1
