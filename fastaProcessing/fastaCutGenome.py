#!/usr/bin/python
""" 

 infName = argv[1]
 bedfName = argv[2]
 
input file is a genome, only one sequence in fasta format
bed file contain the start, end position.

output a fasta file for each line of the bed file.

"""

from sys import argv
from Bio import SeqIO
import sys

if len(argv)<>3:
    sys.exit(__doc__)    


infName = argv[1]
bedfName = argv[2]

bedf = open(bedfName, 'r')
inf = open(infName,'r')

records = SeqIO.parse(inf,'fasta')
for r in records:
    seqId = r.id
    seqName = r.description
    seq = r.seq

for l in bedf:
    start = int(l.split('\t')[1])
    end = int(l.split('\t')[2])
    gene = l.split('\t')[-1].rstrip()
    geneSeq = seq[start:end]

    outf = open("%s_reference.fsa"%gene,'w')
    outf.write(">%s %s_%s-%s\n%s\n\n"%(gene, seqName, start, end, geneSeq)) 
    outf.close()
