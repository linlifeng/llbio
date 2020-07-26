#!/usr/bin/python

'''
1. fasta name
2. save string size (integer, or 'id')

'''

from sys import argv, exit
from Bio import SeqIO

try:
    fname = argv[1]
    f = open(fname, 'r')
    records = SeqIO.parse(f, 'fasta')
    size = argv[2]
except:
    exit(__doc__)

for r in records:
    name = r.description
    sequence = r.seq
    if size == 'id':
        newName = r.id
    else:
        newName = name[:int(size)]
    print ">%s\n%s"%(newName, sequence)



f.close()
