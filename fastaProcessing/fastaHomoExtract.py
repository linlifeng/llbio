#!/usr/bin/python
"""
input:
1. query file
2. db file
3. out file
#(not implemented)4. padding (will look upstream and downstream of the hits)
"""


from Bio.Blast import NCBIStandalone
#from Bio import SearchIO #supposedly the new and up to date way of parsing blast files.
from sys import argv
import os

if len(argv) <> 5:
    os.sys.exit(__doc__)

queryFile = argv[1]
dbFile = argv[2]
outFile = argv[3]
#padding = int(argv[4])

# Format dbFile
if os.path.exists("%s.nin"%dbFile):
    print "--[WARNING]blastdb already formated, using the existing one."
else:
    print "Formatting database..."
    os.system('formatdb -i %s -p F'%dbFile)

# Run BLAST
os.system('blastall -p blastn -i %s -d %s -e 1e-10 -v 100000 -b 100000 -m 0 -o temp.blo -q -2'%(queryFile, dbFile))

# Extract sequeces from blo file
outf = open(outFile, 'w')
blast_parser = NCBIStandalone.BlastParser()
blast_iterator = NCBIStandalone.Iterator(open('temp.blo'), blast_parser)
#blast_iterator = SearchIO.parse(open('temp.blo'),'blast-txt') #if switch to SearchIO, this is the way to go (not working yet)
for hit in blast_iterator:
    for alignment in hit.alignments:
        for hsp in alignment.hsps:
            #print alignment.title
            #print hsp.sbjct_start, hsp.sbjct_end
            #print hsp.sbjct
            outf.write("%s_%s-%s\n%s\n\n"%(alignment.title, hsp.sbjct_start, hsp.sbjct_end, hsp.sbjct))


