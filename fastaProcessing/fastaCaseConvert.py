#!/usr/bin/python

'''
convert the case of fasta file.

1. fasta file name
2. output file name
3. desired case (upper/lower)
'''

from sys import argv, exit
from Bio import SeqIO

if len(argv) <> 4:
    exit(__doc__)

o = open(argv[2],'w')
f = open(argv[1],'r')
case = argv[3].rstrip()
records = SeqIO.parse(f, 'fasta')
for r in records:
    o.write('>' + r.description + '\n')
    if case == 'upper':
        o.write(str(r.seq).upper() + '\n\n')
    elif case == 'lower':
        o.write(str(r.seq).lower() + '\n\n')
    else:
        exit(__doc__)

o.close()
f.close()
