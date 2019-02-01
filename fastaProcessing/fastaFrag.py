#!/usr/bin/env python

'''
convert large sequences into small fragments

1. fasta file
2. fragment size
3. step
'''

from sys import argv, exit
from Bio import SeqIO
from os import system

try:
    fname = argv[1]
    fragSize = int(argv[2])
    step = int(argv[3])
except:
    exit(__doc__)

f = open(fname, 'r')
records = SeqIO.parse(f, 'fasta')

for record in records:
    seqName = record.description
    seqShortName = record.id
    sequence = record.seq
    i = 0
    fragStart = 0
    fragEnd = fragStart + fragSize
    while fragEnd <= len(sequence):
        i += 1
        print ">%s_seg%s\n%s"%(seqShortName, i, sequence[fragStart:fragEnd])
        fragStart = fragStart + step
        fragEnd = fragStart + fragSize
    if not fragStart  >= len(sequence) :
        print ">%s_seg%s\n%s"%(seqShortName, i + 1, sequence[fragStart:len(sequence)])
        

f.close()
