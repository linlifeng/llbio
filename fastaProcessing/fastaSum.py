#!/usr/bin/python
'''
this is an extended version of the fastaLen.py script.(but does not rely on that to work)
takes in a fasta format sequence
print on screen the
id\tlen\tungappendLen\tA-count\tT-count\tC-count\tG-count\tfullName

argv:
1. fastaFname

'''

from Bio import SeqIO
from sys import argv, exit

if len(argv) == 1:
    exit(__doc__)

f = open(argv[1], 'r')

print '\t'.join(['id', 'len', 'ungappedLen', 'a', 't','c','g', 'gc%', 'non-ATGC%', 'fullName'])
for record in SeqIO.parse(f, 'fasta'):
    length = len(record.seq)
    ungapped = record.seq.ungap('-').ungap('~')
    AC = ungapped.lower().count('a')
    TC = ungapped.lower().count('t')
    CC = ungapped.lower().count('c')
    GC = ungapped.lower().count('g')
    cleanedLen = len(ungapped)

    percGC = (float(GC) + float(CC)) / cleanedLen
    percNoneATGC = 1 - (float(GC) + float(CC) + float(AC) + float(TC))/length

    print '\t'.join([record.id, str(length), str(cleanedLen), str(AC), str(TC), str(CC), str(GC), str(percGC), str(percNoneATGC), record.description])
