#!/usr/bin/python

from sys import argv, exit
from Bio import Entrez

Entrez.email = "lifeng.lin@lifetech.com"

f = open(argv[1],'r')
for l in f:
    gid = l.rstrip()
    handle = Entrez.efetch(db="nucleotide", id=gid, rettype='gb')
    found = False
    for r in handle:
        isolate = ''
        if '/organism' in r:
            #print r
            found = True
            #if 'isolate' in r:
            #isolate = r.strip().replace('/','').split('=')[-1]
            print gid+"\t"+r.strip().replace('/','').split('=')[-1]

    if not found:
        print gid+"\t"+'no organism tag found'
