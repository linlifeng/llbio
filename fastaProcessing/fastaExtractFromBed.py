#!/usr/bin/env python

'''
1. fasta file
2. bed file

one should maybe use bedtools getfasta instead:


Tool:    bedtools getfasta (aka fastaFromBed)
Version: v2.25.0
Summary: Extract DNA sequences into a fasta file based on feature coordinates.

Usage:   bedtools getfasta [OPTIONS] -fi <fasta> -bed <bed/gff/vcf> -fo <fasta>


'''

from sys import argv, exit
from Bio import SeqIO
from os import system

try:
    fname = argv[1]
    bfname = argv[2]
except:
    exit(__doc__)



f = open(fname, 'r')
records = SeqIO.parse(f, 'fasta')
seqDict = {}
for record in records:
    seqName = record.description
    seqShortName = record.id
    sequence = record.seq
    seqDict[seqShortName] = sequence
f.close()



f = open(bfname, 'r')
i = 0
for l in f:
    i += 1
    if "track" == l[:5] or '"' == l[0]:
        continue
    segs = l.rstrip().split('\t')
    chrm,start,end = segs[:3]
    if len(segs) > 3:
        name = segs[3]
    else:
        name = 'seq_' + str(i) 
    seq = seqDict[chrm][int(start):int(end)]
    print(">%s\n%s"%(name, seq))
