#!/usr/bin/python

'''
this removes duplicated sequences based on the 'ID' field
basically the first portion of the fasta title before the space
!! retains only the longest sequences from the list with the same ID

'''

from sys import argv, exit
from Bio import SeqIO

if len(argv) == 1:
    exit(__doc__)


inFname = argv[1]
outFname = inFname + '_dupRmd.fsa'
inf = open(inFname,'r')
outf = open(outFname, 'w')
records = SeqIO.parse(inFname, 'fasta')

idSpace = {}
redCount = 0
for record in records:
    if record.id not in idSpace:
        idSpace[record.id] = [record.description, str(record.seq)]
    else:
        if len(str(record.seq).replace('-','').replace('~','')) > len(idSpace[record.id][1].replace('-','').replace('~','')):
            idSpace[record.id] = [record.description, str(record.seq)]
        redCount += 1

for uniqR in idSpace:
        outf.write(">%s\n%s\n\n"%(idSpace[uniqR][0], idSpace[uniqR][1]))

inf.close()
outf.close()

print "--[DONE]Found %s duplicated sequences."%redCount
