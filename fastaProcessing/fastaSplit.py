#!/usr/bin/python
'''
this script separate a multiple sequence fasta file into separate fasta files containing one sequence each.

1. fasta input

'''
from sys import argv, exit
if len(argv) <> 2:
    exit(__doc__)

from Bio import SeqIO

f = open(argv[1], 'r')
records = SeqIO.parse(f, 'fasta')

i = 1
for r in records:
    o = open('%s_individual_seq_%s.fsa'%(argv[1],i),'w')
    SeqIO.write(r,o,'fasta')
    i += 1
    o.close()

f.close()
    
