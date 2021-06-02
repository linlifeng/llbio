#!/usr/bin/env python

'''
1. fasta file as input


returns base composition
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


print "Name\tShortName\tLength\tGC%\tnon-standard_base%\tA\tT\tC\tG\tU\tW\tS\tM\tK\tR\tY\tB\tD\tH\tV\tN\tZ\t-"
for record in records:
    seqName = record.description
    seqShortName = record.id
    sequence = record.seq
    print "%s\t%s\t%s\t%.2f\t%.2f\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s"\
%(seqName, \
seqShortName, \
len(sequence), \
float((sequence.upper().count('C')) + sequence.upper().count('G')) / len(sequence), \
1 - float((sequence.upper().count('C')) + sequence.upper().count('G') + sequence.upper().count('A') + sequence.upper().count('T')) / len(sequence), \
sequence.upper().count('A'), \
sequence.upper().count('T'), \
sequence.upper().count('C'), \
sequence.upper().count('G'), \
sequence.upper().count('U'), \
sequence.upper().count('W'), \
sequence.upper().count('S'), \
sequence.upper().count('M'), \
sequence.upper().count('K'), \
sequence.upper().count('R'), \
sequence.upper().count('Y'), \
sequence.upper().count('B'), \
sequence.upper().count('D'), \
sequence.upper().count('H'), \
sequence.upper().count('V'), \
sequence.upper().count('N'), \
sequence.upper().count('Z'), \
sequence.upper().count('-')
)
