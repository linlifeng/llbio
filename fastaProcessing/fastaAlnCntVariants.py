#!/usr/bin/env python

'''
1. fasta alignment
2. window size
3. step
'''


from sys import argv, exit
from Bio import SeqIO
from os import system, popen


try:
    fname = argv[1]
    windowSize = int(argv[2])
    step = int(argv[3])
except:
    exit(__doc__)

f = open(fname, 'r')
records = SeqIO.parse(f, 'fasta')

ref = []
dic = {}
maxSeqNameLen = 0
i = 0
for record in records:
    seqName = record.description
    seqShortName = record.id
    sequence = record.seq
    dic[seqName] = sequence
    if i == 0:
        ref = [seqShortName, sequence]
    if len(seqShortName) > maxSeqNameLen:
        maxSeqNameLen = len(seqShortName)
    i += 1
f.close()


alnLen = len(ref[1])



# start drawing
windowStart = 0
while windowStart < alnLen: 
    windowEnd = windowStart + windowSize
    if windowEnd > alnLen:
        windowEnd = alnLen
    windowName = "%s_%s"%(windowStart, windowEnd)
    versions = []
    for seqName in dic:
        sequence = dic[seqName]
        frag = sequence[windowStart:windowEnd]
        versions.append(frag)
    print "%s\t%s"%(windowName, len(set(versions)))
    windowStart = windowEnd
