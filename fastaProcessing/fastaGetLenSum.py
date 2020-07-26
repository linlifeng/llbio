#!/usr/bin/python

'''
get the total sequence length of a fasta file that contain multiple sequences
1. fasta file name
'''

from sys import argv, exit
from Bio import SeqIO

f = open(argv[1], 'r')
records = SeqIO.parse(f,'fasta')

lenTotal = 0
seqCount = 0
for r in records:
    seqCount += 1
    lenTotal += len(r.seq)

print "Number of Seqs:\t" + str(seqCount)
print "Total length:\t" + str(lenTotal)
print "Average length:\t" + str(lenTotal/float(seqCount))
