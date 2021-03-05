#!/usr/bin/env python

'''
1. fasta alignment
2. color bases? (y/n)
3. mask matching bases? (y/n)
'''


from sys import argv, exit
from Bio import SeqIO
from os import system, popen


try:
    fname = argv[1]
    color = argv[2].upper()
    mask = argv[3].upper()
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

    if mask.upper() == 'Y':
        maskedSeq = ''
        for i in range(len(sequence)):
            base = sequence[i]
            if base.upper() == ref[1][i].upper() and not base == '-':
                base = '.'
            maskedSeq += base
        dic[seqName] = maskedSeq

    i += 1
f.close()


## display settings
# set name width
if maxSeqNameLen < 50:
    tagWidth = maxSeqNameLen
else:
    tagWidth = 50
alnLen = len(ref[1])

# automatic windown size
outputH, outputW = popen('stty size', 'r').read().split()
windowSize = int(outputW) - tagWidth - 8


# start drawing
windowStart = 0
while windowStart < alnLen:
    windowEnd = windowStart + windowSize
    if windowEnd > alnLen:
        windowEnd = alnLen

    offset = windowEnd - windowStart - len(str(windowStart)) - len(str(windowEnd))
    print("%*s\t%s"%(tagWidth, "Pos", windowStart + 1) + ' '*offset + str(windowEnd))
    print("%*s\t%s"%(tagWidth, "Ref", ref[1][windowStart:windowEnd]))

    for seqName in dic:
        sequence = dic[seqName]
        frag = sequence[windowStart:windowEnd]
        coloredFrag = str(frag).upper()\
.replace('A','\033[43mA\033[0m')\
.replace('T','\033[44mT\033[0m')\
.replace('C','\033[45mC\033[0m')\
.replace('G','\033[46mG\033[0m')
        if color.upper() == 'Y' or color.upper() == 'YES':
            print("%*s\t%s"%(tagWidth, seqName[:tagWidth], coloredFrag))
        else:
            print("%*s\t%s"%(tagWidth, seqName[:tagWidth], frag))

    windowStart = windowEnd
    print("\n")
