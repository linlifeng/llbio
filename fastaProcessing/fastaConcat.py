#!/usr/bin/python

'''
1. fasta file
2. padding length
    integer. The number of empty 'N' bases added between the concatenated sequences
3. chrName
'''

from sys import argv, exit
from Bio import SeqIO
from os import path, system

try:
    fname = argv[1]
    pad = int(argv[2])
    chrm = argv[3]
except:
    exit(__doc__)


f = open(fname, 'r')
of = open(fname + '_concatenated.fsa', 'w')
ofbed = open(fname + '_concatenated.bed', 'w')


# initialize values
records = SeqIO.parse(f, 'fasta')
concatSeq = ''
segCoords = {}
start = 0

# populating results
for r in records:
    concatSeq += r.seq
    end = start + len(r.seq)
    segCoords[r.id] = [start,end]
    start = end
    if pad > 0:
        concatSeq += 'N' * pad
        start += pad

# write out
of.write(">%s\n%s\n"%(chrm, concatSeq))
for seg in segCoords:
    ofbed.write("%s\t%s\t%s\t%s\n"%(chrm, segCoords[seg][0], segCoords[seg][1], seg))



f.close()
of.close()
ofbed.close()

