#!/usr/bin/python
'''
1. fasta file name
2. prefix
'''

from sys import argv, exit
from Bio import SeqIO
from os import path, system

try:
    fname = argv[1]
    f = open(fname, 'r')
    records = SeqIO.parse(f, 'fasta')
    prefix = argv[2]

except:
    exit(__doc__)


#create uniq sequence library
useqs = {}
for r in records:
    if r.seq in useqs:
        #useqs[r.seq].append((r.id, r.description))
        useqs[r.seq].append(r.id)
    else:
        #useqs[r.seq] = [(r.id, r.description)]
        useqs[r.seq] = [r.id]

'''
#QC
print len(useqs)
for useq in useqs:
    print useq
    print len(useqs[useq])
'''

#output
uniqFsa = open(path.basename(fname) + '_uniq.fsa', 'w')
lookupF = open(path.basename(fname) + '_lookUp.tab', 'w')
uniqBed = open(path.basename(fname) + '_uniq.bed', 'w')

i = 1
for useq in useqs:
    uniqFsa.write(">%s_unqVar%s\n%s\n"%(prefix, i, useq))
    for item in useqs[useq]:
        lookupF.write("%s\t%s_unqVar%s\t%s\n"%(item, prefix, i, useq))
    uniqBed.write("%s_unqVar%s\t%s\t%s\t.\tGENE_ID=%s\n"%(prefix, i, '1', len(useq), ','.join(useqs[useq])))
    i += 1


uniqFsa.close()
lookupF.close()
uniqBed.close()
