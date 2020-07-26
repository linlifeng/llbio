#!/usr/bin/python
'''
1. fastaName
2. fragSize
3. step
4. prefix of fragments
'''

def getUniCnt(List):
    return len(set(List))

def fastaHash(fastaFname):
    fastaDict = {}
    from Bio import SeqIO
    fastaF = open(fastaFname, 'r')
    records = SeqIO.parse(fastaF, 'fasta')
    longestLen = 0
    for r in records:
        fastaDict[r.description] = r.seq
        if len(r.seq) > longestLen:
            longestLen = len(r.seq)
    return fastaDict, longestLen

from sys import argv,exit

if len(argv) <> 5:
    exit(__doc__)

fastaDict, length = fastaHash(argv[1])
fragSize = int(argv[2])
step = int(argv[3])
prefix = argv[4]

counts = {}
pos = 0
while pos < length - fragSize:
    #print pos
    fullList = []
    for seqName in fastaDict:
        seg = fastaDict[seqName][pos:pos+fragSize]
        if not seg[0] == '-' and not  seg[-1] == '-': #for start and end positions, the dangling ends exaggerates the primer count.
            fullList.append(seg)
        #print pos+fragSize, seg
    if len(fullList) == 0:
        fullList = ['emptyWindow']
    counts[pos]=(str(fullList[0]), str(getUniCnt(fullList)))
    pos += step

for pos in counts:
    start = int(pos) + 1
    end = int(pos) + int(fragSize)
    print "%s_%s-%s\t%s"%(prefix, start, end, '\t'.join(counts[pos]))

