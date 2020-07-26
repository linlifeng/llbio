#!/usr/bin/python

'''
1. fasta file
2. base to be replaced
3. base to replace with
'''

from sys import argv, exit
from Bio import SeqIO
from os import path, system

try:
    fname = argv[1]
    tb = argv[2]
    rb = argv[3]
except:
    exit(__doc__)


f = open(fname, 'r')
r = SeqIO.parse(f, 'fasta')
for record in r:
    sequence = str(record.seq)
    name = record.description
    newseq = sequence.replace(tb, rb)
    print ">%s\n%s"%(name, newseq)


f.close()

