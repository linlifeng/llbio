#!/usr/bin/python
'''
this script calles fastaHomoExtract.py

1. query fasta (can contain multiple seqs)
2. db fasta (will be formated for BLAST)
3. output folder
'''


from sys import argv, exit
from Bio import SeqIO
import os

if len(argv) <> 4:
    exit(__doc__)

qFname = argv[1]
dbFname = argv[2]
oFolder = argv[3]
os.system("mkdir %s"%oFolder)
tmpFname = 'tmp.homoExtract.fsa'

qf = open(qFname,'r')
records = SeqIO.parse(qf,'fasta')
for record in records:
    print "processing %s..."%record.id
    outFname = "%s_extracted.fsa"%record.id
    tmpf = open(tmpFname, 'w')
    tmpf.write(">%s\n%s\n"%(record.description, record.seq))
    tmpf.close()
    outPath = oFolder + '/' + outFname
    os.system("fastaHomoExtract.py %s %s %s"%(tmpFname, dbFname, outPath))
qf.close()

os.system("rm %s"%tmpFname)
os.system("rm temp.blo")     
