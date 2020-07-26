#!/usr/bin/python

from sys import argv, exit
from Bio import SeqIO

f = open(argv[1],'r')
records = SeqIO.parse(f,'fasta')

for r in records:
    seq = str(r.seq).replace('-', 'N')
    print(">%s\n%s\n"%(r.description, seq))

f.close()
    
