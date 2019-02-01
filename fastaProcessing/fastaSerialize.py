#!/usr/bin/env python

'''
1. fasta file

convert a fasta file like this:
>seq1
atcg
>seq2
ttgca

into this:
seq1    1   a
seq1    2   t
seq1    3   c
seq1    4   g
seq2    1   t
seq2    2   t
seq2    3   g
seq2    4   c
seq2    5   a


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
    i = 1
    seqName = record.description
    seqShortName = record.id
    sequence = record.seq
    for base in sequence:
        print "%s\t%s\t%s"%(seqShortName, i, base)
        i += 1

