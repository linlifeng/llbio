#!/usr/bin/python
'''
This is to clean up the extracted alignment so it contains only the full length sequences. 
This removes the following from alignment:
1.sequences start with '-'
2.sequences end with '-'
3.sequences with '-' account for over 20% of the full length.

Arguments:
1. alignment fasta file ('-' indicates gaps)

'''
from sys import argv, exit
import os
from Bio import SeqIO

if len(argv) <> 2:
    exit(__doc__)

inFname = argv[1]
outFname = inFname + '_partialRemoved.fasta'

inf = open(inFname, 'r')
outf = open(outFname, 'w')
records = SeqIO.parse(inf, 'fasta')
for record in records:
    spCount = record.seq.count('-')
    fullLen = len(record.seq)
    missedPortion = float(spCount)/float(fullLen)
    #print spCount, fullLen, missedPortion
    if record.seq[0] == '-' or record.seq[-1] == '-' or missedPortion > 0.2:
        continue
    else:
        outf.write(">%s\n%s\n\n"%(record.description, record.seq))
inf.close()
outf.close()
