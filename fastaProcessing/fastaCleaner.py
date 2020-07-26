#!/usr/bin/python

'''
remove anything that contains non-atcg letters

1. fasta file

write out _cleaned.fsa file
print on screep the bad ones (so one can redirect to another file)
'''

from sys import argv, exit
from Bio import SeqIO
from os import path

try:
    fname = argv[1]
    f = open(fname, 'r')
except:
    exit(__doc__)

oname = path.basename(fname)+'_cleaned.fsa'
o = open(oname, 'w')
records = SeqIO.parse(f, 'fasta')
for r in records:
    bad = False
    s = r.seq
    for letter in s:
        if letter not in 'atcgATCG':
            bad = True
            break
    if not bad:
        o.write(">%s\n%s\n"%(r.description, r.seq))
    else:
        print "%s\t%s"%(r.id, r.seq)

o.close()
f.close()
