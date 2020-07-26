#!/usr/bin/python

'''
this script calls NCBIGFFFeatureExtract.py, which takes in GFF, fna, ob and generate fasta and tab files.
this script takes in a ncbi genome ftp folder (assuming both gff and fna files are present), and download and run the gff extract script

argv:
1. remote ncbi genome folder name
2. ob

'''
from sys import argv,exit
from os import system,path
from ftplib import FTP
import urllib

if len(argv) == 1:
    exit(__doc__)

self, ftpFolder, ob = argv 

ftp = FTP('ftp.ncbi.nlm.nih.gov')
ftp.login()

directory = ftpFolder.replace('ftp://ftp.ncbi.nlm.nih.gov', '')
ftp.cwd(directory)
#ftp.retrlines('LIST')
files = ftp.nlst()
fnaCount = 0
gffCount = 0
for m in files:
    if 'genomic.fna.gz' in m:
        fnaFileLink = "ftp://ftp.ncbi.nlm.nih.gov%s/%s"%(directory, m)
        fnaCount += 1
    if 'genomic.gff.gz' in m:
        gffFileLink = "ftp://ftp.ncbi.nlm.nih.gov%s/%s"%(directory, m)
        gffCount += 1
print "downloading %s for %s"%(fnaFileLink, ob)
fnaSavedName = "%s_genomic.fna.gz"%(ob.rstrip())
gffSavedName = "%s_genomic.gff.gz"%(ob.rstrip())
urllib.urlretrieve(fnaFileLink, fnaSavedName)
urllib.urlretrieve(gffFileLink, gffSavedName)

system('gunzip %s'%fnaSavedName)
system('gunzip %s'%gffSavedName)

ftp.quit()

system('/rhome/linl2/lifeng_src/NCBIGFFFeatureExtract.py %s %s %s'%(gffSavedName.replace('.gz',''), fnaSavedName.replace('.gz',''), ob.rstrip()))
