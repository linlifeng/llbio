#!/usr/bin/python

'''
1. fasta file with a list of sequence
2. a text file contain a list of keywords
3. exact matches (y/n)
output a subset of the input fasta file that does not contain the keywords
into a _subtracted.fsa file
'''

from sys import argv, exit, stdout
from os import system,path
from Bio import SeqIO

if len(argv) == 1:
    exit(__doc__)

inFname = argv[1]
giFname = argv[2]
exact = argv[3].upper()
outFname = path.basename(inFname) + '_subtracted.fsa'
inf = open(inFname, 'r')
gif = open(giFname, 'r')
outf = open(outFname,'w')

giList = {}
for l in gif:
    giList[(l.replace('\n',''))] = 1
print "Loaded %s identifiers from the query file..."%len(giList)

records = SeqIO.parse(inf,'fasta')
seqCount = sum(1 for _ in records)
print "Loaded %s sequences in fasta file..."%seqCount

foundCnt = 0
counter = 0
inf = open(inFname, 'r')
records = SeqIO.parse(inf, 'fasta')
for r in records:
    excl = False
    for l in giList:
        if exact == 'N':
            if l in r.id or l + ' ' in r.id or l + '\t' in r.id or l + ':' in r.id or l == r.id:
                excl = True
        elif exact == 'Y':
            if l == r.id or l == r.description:
                excl = True
        else:
            exit(__doc__ + "\nunrecognized parameter for exact %s"%exact)

    if not excl:
        SeqIO.write(r, outf, 'fasta')
        foundCnt += 1
    counter += 1
    '''
    if counter % (seqCount/20) == 0:
        #print "--roughly %s finished"%counter/(seqCount/10)
        stdout.write("%s%% "%(counter / (seqCount/100)))
        #if foundCnt % 100 == 0:
        #    print "Found %s so far..."%foundCnt
    '''
inf.close()
gif.close()
outf.close()

