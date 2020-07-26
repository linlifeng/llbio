#!/usr/bin/python

'''
!! requires fastaCutAlignment.py

1. fasta alignment file
2. coordinate list: first two columns: start, end
'''

from sys import argv, exit
from os import system, path

try:
    fname = argv[1]
    cname = argv[2]
except:
    exit(__doc__)

c = open(cname,'r')

for l in c:
    start, end = l.rstrip().split('\t')[:2]
    #print fname, start, end
    cmd = "fastaCutAlignment.py %s %s %s > %s_%s_%s.tab"%(fname, start, end, path.basename(fname), start, end)
    #print cmd
    system(cmd)
