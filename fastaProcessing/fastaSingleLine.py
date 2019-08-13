#!/usr/bin/python
'''
1. fasta file
'''

from sys import argv, exit

try:
    fastaf = open(argv[1], 'r')
except:
    exit(__doc__)


seq = ''
for l in fastaf:
    if '>' == l[0]:
        print seq
        print l.rstrip()
        seq = ''
    else:
        seq += l.rstrip()
print seq
