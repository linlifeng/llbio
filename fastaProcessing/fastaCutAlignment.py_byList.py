#!/usr/bin/python
'''
input two files
1. fasta file
2. cood list ( start, end pairs)

calls fastaCutAlignment.py

'''

from sys import argv, exit
from os import system

try:
    fname = argv[1]
    cname = argv[2]

except:
    exit(__doc__)


f = open(cname,'r')

for l in f:
    segs = l.rstrip().split('\t')
    start = int(segs[0])
    end = int(segs[1])
    system("fastaCutAlignment.py %s %s %s > %s_%s_%s.tab"%(fname, start, end, fname, start, end))
    system("fasta2tab.py %s_%s_%s.tab"%(fname, start, end))
    


f.close()
