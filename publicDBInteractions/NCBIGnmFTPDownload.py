#!/usr/bin/python

'''

1. link file name. format:
    spName\tlink\tlevel
    (this file can be automatically generated using the NCBIGnmGetFTPLink.py script)
2. destination folder

'''
from sys import argv,exit
from os import system,path
from ftplib import FTP
import urllib

if len(argv) == 1:
    exit(__doc__)

self, inFname, destFolder = argv 

ftp = FTP('ftp.ncbi.nlm.nih.gov')
ftp.login()

f = open(argv[1],'r')
blastDBListF = open("%s.dbl"%path.basename(argv[1]),'w')
for l in f:
    fnaCount = 0
    link = l.split('\t')[1]
    org = l.split('\t')[0]
    if link in ['no_genome', 'na']:
        continue
    directory = link.replace('ftp://ftp.ncbi.nlm.nih.gov', '')
    ftp.cwd(directory)
    #ftp.retrlines('LIST')
    files = ftp.nlst()
    for m in files:
        if 'genomic.fna.gz' in m:
            fileLink = "ftp://ftp.ncbi.nlm.nih.gov%s/%s"%(directory, m)
            fnaCount += 1
    print "downloading %s for %s"%(fileLink, org)
    savedName = "%s/%s_genomic.fna.gz"%(destFolder.rstrip(), org.replace(' ','_').replace('/','_').replace('(','_').replace(')','_'))
    if not path.isfile(savedName.replace('.gz','.nin')):
        urllib.urlretrieve(fileLink, savedName)
        system('gunzip %s'%savedName)
        system('formatdb -i %s -p F -o T'%savedName.replace('.gz',''))
    else:
        print "%s already exists. Skipping..."%savedName
    blastDBListF.write(path.abspath(savedName.replace('.gz','')) + '\n' )

ftp.quit()
blastDBListF.close()

print "Genome Downloads Done...file generated: %s.dbl"%path.basename(argv[1])
