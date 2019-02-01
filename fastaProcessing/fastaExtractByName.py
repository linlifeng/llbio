#!/usr/bin/env python

'''
1. fasta file
2. keyword to search

any entry that contains the keyword in their sequence name will be returned.

alternatively, use samtools:

xargs samtools faidx test.fa < names.txt


'''

from sys import argv, exit
from Bio import SeqIO
from os import system

try:
    fname = argv[1]
    key = argv[2]
except:
    exit(__doc__)

f = open(fname, 'r')
records = SeqIO.parse(f, 'fasta')

for record in records:
    seqName = record.description
    seqShortName = record.id
    sequence = record.seq
    if key in seqName:
        print ">%s\n%s"%(seqName, sequence)

f.close()
