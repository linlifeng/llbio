#!/usr/bin/python
'''
usage:
~ Accession Number

print on screen

'''
"""Fetch GenBank entries for given accessions. 

USAGE:
  <self> A22237 A22239 A32021 A32022 A33397 > out.gb
or
  cat ids | python acc2gb.py > out.gb

DEPENDENCIES:
Biopython
"""

from sys import argv,exit,stdout,stderr
from Bio import Entrez

#define email for entrez login
db           = "nuccore"
Entrez.email = "some_email@somedomain.com"
retformat = 'fasta'
#retformat = 'gb'
#load accessions from arguments
if len(argv) > 1:
  accs = argv[1:]
else: #load accesions from stdin  
#  accs = [ l.strip() for l in sys.stdin if l.strip() ]
  exit(__doc__)
#fetch
#stderr.write( "Fetching %s entries from GenBank: %s\n" % (len(accs), ", ".join(accs[:10])))
for i,acc in enumerate(accs):
  try:
    stderr.write( " %9i %s          \r" % (i+1,acc))  
    handle = Entrez.efetch(db=db, rettype=retformat, id=acc)
    #print output to stdout
    stdout.write(handle.read())
  except:
    stderr.write( "Error! Cannot fetch: %s        \n" % acc)  
