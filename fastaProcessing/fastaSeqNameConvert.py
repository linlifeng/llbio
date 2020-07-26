#!/usr/bin/python

'''
1. fasta file

this convert the ncbi downloaded fasta format into something like:
>accession\tgi|xxxx||accession descriptions
sequence

i.e. move the accession portion to the front of the sequence description to be used as chr name later
'''

from sys import argv, exit
from os import system, path
from Bio import SeqIO

if len(argv) <> 2:
    exit(__doc__)

f = open(argv[1],'r')
records = SeqIO.parse(f, 'fasta')
o = open(path.basename(argv[1]) + '_seqName_converted.fsa', 'w')

for r in records:
    desc = r.description
    accession = r.id.split('|')[3].split('.')[0]
    o.write(">%s %s\n%s\n"%(accession, desc, r.seq))

f.close()
o.close()
