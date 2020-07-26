#!/usr/bin/python
'''
1. fname
2. remain length

truncate the sequence name, saving only the given length
'''

from sys import argv, exit
from Bio import SeqIO

try:
    fname = argv[1]
    length = int(argv[2])
    f = open(fname, 'r')
    records = SeqIO.parse(f,'fasta')
except:
    exit(__doc__)


for s in records:
    name = s.description[:length]
    print ">%s\n%s"%(name, s.seq)
    

f.close()
