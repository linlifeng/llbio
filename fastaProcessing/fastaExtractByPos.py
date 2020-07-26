#!/usr/bin/python

'''
USAGE:
    ~ fastaFname cordFname(bedFormat) base(1/0) windowSize
    bed:
        chr start   end

print on screen
'''

from sys import argv,exit
from Bio import SeqIO
try:
    fastaFname = argv[1]
    cordFname = argv[2]
    baseForm = int(argv[3])
    window = int(argv[4])
except:
    exit(__doc__)

f = open(fastaFname,'r')
records = SeqIO.parse(f, 'fasta')
seqHash = {}
for r in records:
    seqHash[r.id] = r.seq
f.close()

f = open(cordFname, 'r')
for l in f:
    if 'track name=' in l:
        continue
    segs = l.rstrip().split('\t')
    chro, start, end = segs[:3]
    if len(segs) > 3:
        seqName = segs[3]
    else:
        seqName = "%s_%s_%s"%(chro, start, end)
    if int(end) > int(start):
        sequence = seqHash[chro][int(start) - baseForm - window: int(end) + window]
        print ">%s\n%s"%(seqName, sequence)
    else:
        sequence = seqHash[chro][int(end) - baseForm - window : int(start) + window].reverse_complement()
        print ">%s_RC\n%s"%(seqName, sequence)
    
