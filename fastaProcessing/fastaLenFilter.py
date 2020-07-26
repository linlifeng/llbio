#!/usr/bin/python
'''
this filter out zero length sequences from a fasta file
(some times ncbi downloads contain master records that doesn't have any sequences, which breaks the blast foramtting)

1. fasta file
2. min len
3. max len
'''


from Bio import SeqIO
from sys import argv, exit

if len(argv) == 1:
    exit(__doc__)

infName = argv[1]
minLen = int(argv[2].rstrip())
maxLen = int(argv[3].rstrip())
outName = "%s_%s_%s_lengthfiltered.fsa"%(infName, minLen, maxLen)
logName = 'fastaLenFilter.log'

inf = open(infName, 'r')
outf = open(outName, 'w')
logf = open(logName, 'w')
records = SeqIO.parse(inf, 'fasta')

for r in records:
    if len(r.seq) < minLen or len(r.seq) > maxLen:
        #print "%s have zero length"%r.id
        logf.write(r.id + '\n')
    else:
        SeqIO.write(r, outf, 'fasta')
