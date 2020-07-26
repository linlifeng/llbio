#!/usr/bin/python

'''
1. fasta file
2. sequence output prefix
'''

from sys import argv, exit
from Bio import SeqIO
from os import path

if len(argv) <> 3:
    exit(__doc__)

fname = argv[1]
prefix = argv[2]
oname = path.basename(fname) + '_uniqSet.fsa'
ocname = path.basename(fname) + '_uniqCount'
uniqSet = {}
f = open(fname,'r')
records = SeqIO.parse(f,'fasta')
for r in records:
    if str(r.seq) in uniqSet.keys():
        uniqSet[str(r.seq)][0] += 1
    else:
        uniqSet[str(r.seq)] = [1, r.description]
f.close()

o = open(oname,'w')
oc = open(ocname,'w')
i = 1
for key in uniqSet:
    o.write(">%s_%s\tcount:%s\treference:%s\n%s\n"%(prefix, i, uniqSet[key][0], uniqSet[key][1], key))
    oc.write("%s_%s\t%s\n"%(prefix, i, uniqSet[key][0]))
    i += 1

o.close()
oc.close()
