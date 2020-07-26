#!/usr/bin/python

'''
1. fasta file
2. chromosome prefix (added to  the chr numbers. optional)
3. convert file (optional)
    first two cols need to be chr# and key (could be gi or accession or anything unique in the seq name)
'''

from sys import argv, exit
from os import system, path
from Bio import SeqIO

if len(argv) == 1:
    exit(__doc__)

try:
    fsaFname = argv[1]
    chrPrefix = argv[2]
except:
    exit(__doc__)

fsaF = open(fsaFname,'r')
records = SeqIO.parse(fsaF,'fasta')
if len(argv) == 4:
    covFname = argv[3]
    covF = open(covFname, 'r')

    convert = {}
    for l in covF:
        segs = l.split('\t')
        convert[segs[1]] = segs[0]

    for r in records:
        for c in convert.keys():
            if c.rstrip() in r.description:
                #print ">%s%s\t%s\n%s"%(chrPrefix, convert[c], r.description, r.seq)
                print ">%s%s\n%s"%(chrPrefix, convert[c], r.seq)
elif len(argv) == 3:
    #print "[WARNING] no conversion file give, naming consecutively"
    i = 1
    for r in records:
        #print ">%s%s\t%s\n%s"%(chrPrefix, i, r.description, r.seq)
        #print ">%s%s\n%s"%(chrPrefix, i, r.seq)
        print ">%s%s\n%s"%(chrPrefix, r.description, r.seq)
        i += 1
else:
    exit(__doc__)
