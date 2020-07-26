#!/usr/bin/python
'''
!!!!NOT FINISHED, DO NOT USE!!!!

for similary functions, use fastaLen + fasta2tab + updateQuery + cut

1. fasta file name
2. asc/des
'''

from sys import argv,exit
from Bio import SeqIO

try:
    fname = argv[1]
    order = argv[2]
except:
    exit(__doc__)


f = open(fname,'r')
records = SeqIO.parst(f,'fasta')

for r in records:
    seqName = r.description
    sequence = r.seq
    

f.close()

