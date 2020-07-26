#!/usr/bin/python
'''
1. input file, fasta format

auto detects input format.
if tab, convert to fasta
if fsa, convert to tab

'''
from Bio import SeqIO
from sys import argv,exit
from os import path

if len(argv) == 1:
    exit(__doc__)

inFname = argv[1]
inFasta = False

for l in open(inFname, 'r'):
    if l[0] == '>':
        print "this input is detected as a fasta format. Converting to tab."
        inFasta = True
        break

if inFasta:
    outFname = path.basename(inFname) + '.tab'

    inf = open(inFname, 'r')
    outf = open(outFname, 'w')
    records = SeqIO.parse(inf, 'fasta')

    for record in records:
         outf.write("%s\t%s\n"%(record.description, record.seq))

else:
    print "this input is detected as non-fasta format. Converting to fasta."
    outFname = path.basename(inFname) + '.fsa'

    inf = open(inFname, 'r')
    outf = open(outFname, 'w')

    for l in inf:
        name,seq = l.rstrip().split('\t')[:2]
        outf.write(">%s\n%s\n"%(name,seq))

inf.close()
outf.close()
