#!/usr/bin/python
'''
1. fasta name
2. primer tab file name
    name    fprimer rprimer
'''


from sys import argv, exit
from os import path
from Bio import SeqIO

try:
    faFname = argv[1]
    prFname = argv[2]
except:
    exit(__doc__)


#create primer dict
fdic = {}
rdic = {}

prF = open(prFname, 'r')
for l in prF:
    segs = l.rstrip().split('\t')
    name, fseq, rseq = segs[:3]
    fdic[fseq] = 1
    rdic[rseq] = 1
prF.close()

faF = open(faFname, 'r')
of = open(path.basename(faFname) + 'primerTrimmed.fsa', 'w')
records = SeqIO.parse(faF, 'fasta')
for r in records:
    name, sequence, rc = r.description, str(r.seq), str(r.seq.reverse_complement())
    #print sequence
    #print rc
    ftrim = False
    rtrim = False
    for fp in fdic:
        if sequence.find(fp) == 0:
            sequence = sequence[len(fp):]
            ftrim = True
            forward = fp
            break

    for rp in rdic:
        if rc.find(rp) == 0:
            cur = len(sequence) - len(rp)
            sequence = sequence[:cur]
            rtrim = True
            reverse = rp
            break
    #print "%s\n%s\n%s"%(forward, reverse, sequence)

    if not ftrim:
        print "no fprimer found for %s\n%s"%(name, sequence)
    elif not rtrim:
        print "no rprimer found for %s\n%s"%(name,sequence)
    else:
        of.write(">%s_primerTrimmed\n%s\n"%(name, sequence))
of.close()
