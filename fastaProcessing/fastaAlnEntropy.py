#!/usr/bin/env python

'''
1. fasta file

simply uses skbio to calculate shannon diversity of each base in the aligned sequence
'''

from sys import argv, exit
#from Bio import SeqIO
from os import system
import skbio
from io import StringIO

try:
    fname = argv[1]
except:
    exit(__doc__)
#mySeqs = skbio.io.read(fname, format='fasta')

f = open(fname, 'r')
fl = []
for l in f:
    if '>' == l[0]:
        fl.append(l)
    else:
        fl.append(l.replace('?', 'N').upper())
myAln = skbio.TabularMSA.read(fl, constructor=skbio.DNA)

# print out shannon diversity
shannonDs = myAln.conservation(metric='inverse_shannon_uncertainty', degenerate_mode='nan', gap_mode='include')
i = 1
for shannonD in shannonDs:
    print("\t".join([str(i), str(shannonD)]))
    i += 1
######


'''
for attr in dir(myAln):
    if '_' == attr[0]:
        continue
    print(attr)
'''
'''
records = SeqIO.parse(f, 'fasta')

for record in records:
    seqName = record.description
    seqShortName = record.id
    sequence = record.seq

    length = len(sequence)
    start = 0
    while start < length:
        end = start + windowSize + 1
        sub_seq = sequence[start:end] 
        lisfreq1=[sub_seq.count(base)*1.0/len(sub_seq) for base in ["A", "C","G","T"]]
        print seqName, start, end, lisfreq1
        start += step
f.close()
'''
'''
for a in myAln:
    print(a.metadata['id'])
    print(dir(a.positional_metadata))
    for attr in dir(a):
        if not '_' == attr[0]:
            print(attr)
    exit()
'''
