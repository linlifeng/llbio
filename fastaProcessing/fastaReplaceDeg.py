#!/usr/bin/python
'''
1. fasta fname
2. replace with?
'''

from sys import argv,exit
from Bio import SeqIO

try:
    fname = argv[1]
    repl = argv[2]
except:
    exit(__doc__)

f = open(fname, 'r')
records = SeqIO.parse(f,'fasta')

for r in records:
    seq = r.seq
    newSeq = ''
    for l in seq:
        if l.lower() not in ['a','t','c','g']:
            newSeq += repl
        else:
            newSeq += l
    print ">%s\n%s\n"%(r.description, newSeq)

    
