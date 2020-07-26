#!/usr/bin/python
'''
args:
1. gff file name
2. genome fna file name
3. outBase

produces the following files:
<outbase>_genes.fsa
<ob>_cds.fsa
<ob>_genes.tab
<ob>_cds.tab

'''

from sys import argv, exit
from Bio import SeqIO

if len(argv) <> 4:
    exit(__doc__)

gffFname = argv[1]
fnaFname = argv[2]
ob = argv[3]

gffF = open(gffFname,'r')
fnaF = open(fnaFname, 'r')
genesFsaOut = open("%s_genes.fsa"%ob,'w')
cdsFsaOut = open("%s_cds.fsa"%ob,'w')
genesTabOut = open("%s_genes.tab"%ob,'w')
cdsTabOut = open("%s_cds.tab"%ob, 'w')

genomeSeqs = SeqIO.parse(fnaF, 'fasta')
seqDict = {}
for seq in genomeSeqs:
    genomeDesc = seq.description
    genomeSeq = seq.seq
    seqDict[seq.id] = [genomeDesc, genomeSeq]

for l in gffF:
    if len(l) == 0 or l[0] == '#':
        continue
    segs = l.split('\t')
    seqID, featType, featStart, featEnd = segs[0], segs[2], int(segs[3]), int(segs[4])
    if featStart > featEnd:
        featStart, featEnd = featEnd, featStart
    segSeq = seqDict[seqID][1][featStart:featEnd]
#    print segs
    if featType == 'gene':
        genesFsaOut.write(">%s:%s-%s\n%s\n"%(seqID, featStart, featEnd, segSeq)) 
        genesTabOut.write("%s\tgeneFeature\t%s\t%s\t%s\n"%(seqDict[seqID][0], featStart, featEnd, segSeq))
        #print ">%s|geneFeature_%s-%s\n%s\n"%(genomeDesc, featStart, featEnd, segSeq)
    if featType.lower() == 'cds':
        cdsFsaOut.write(">%s:%s-%s\n%s\n"%(seqID, featStart, featEnd, segSeq))
        cdsTabOut.write("%s\tCDSFeature\t%s\t%s\t%s\n"%(seqDict[seqID][0], featStart, featEnd, segSeq))
        #print ">%s|CDSFeature_%s-%s\n%s\n"%(genomeDesc, featStart, featEnd, segSeq)

genesFsaOut.close()
cdsFsaOut.close()
genesTabOut.close()
cdsTabOut.close()

gffF.close()
fnaF.close()
