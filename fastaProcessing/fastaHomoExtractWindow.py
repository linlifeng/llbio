#!/usr/bin/python
"""
input:
1. query file
2. db file
3. padding

input query could contain multiple sequences.
when two query hit the same position, the hit that is covered by the other is ommited

this also print out sequence that are in the same strand, reverse complementing the rsp from the other direction, for ease of alignment.

"""


from Bio.Blast import NCBIStandalone
#from Bio import SearchIO #supposedly the new and up to date way of parsing blast files.
from sys import argv
import os


def formatdb(dbFile):
    if os.path.exists("%s.nin"%dbFile):
        return "--[WARNING]blastdb already formated, using the existing one."
    else:
        os.system('formatdb -i %s -p F'%dbFile)
        return "OK"

def looseBLAST(queryFile, dbFile):
    formatdb(dbFile)
    os.system('blastall -p blastn -i %s -d %s -e 1e-10 -v 100000 -b 100000 -m 0 -o temp.blo -q -2'%(queryFile, dbFile))
    return "temp.blo"

def getCoordinatesFromBlo(bloFname, padding):
    '''
    # Extract coordinates from blo file
    '''
    coord = {}

    #outf = open(outFile, 'w')
    blast_parser = NCBIStandalone.BlastParser()
    blast_iterator = NCBIStandalone.Iterator(open('temp.blo'), blast_parser)
    #blast_iterator = SearchIO.parse(open('temp.blo'),'blast-txt') #if switch to SearchIO, this is the way to go (not working yet)
    for hit in blast_iterator:
        for alignment in hit.alignments:
            for hsp in alignment.hsps:
                #print alignment.title
                #print hsp.sbjct_start, hsp.sbjct_end
                #print hsp.sbjct
                #outf.write("%s_%s-%s\n%s\n\n"%(alignment.title, hsp.sbjct_start, hsp.sbjct_end, hsp.sbjct))
                new = True
                fullName = alignment.title.replace('>','')
                if fullName in coord.keys() and hsp.sbjct_start >= coord[fullName][0] and hsp.sbjct_end <= coord[fullName][1]:
                    new = False
                if new:
                    coord[fullName] = [hsp.sbjct_start, hsp.sbjct_end]
    return coord

def getSeqByCoord(fastaFname, coord, padding):
    '''
    coord is a dictionary with the format:
        fullName: [start, end]
    '''
    from Bio import SeqIO
    f = open(fastaFname,'r')
    records = SeqIO.parse(f,'fasta')
    
    extractedSegs = {}    

    for r in records:
        for name in coord.keys():
            if r.description == name:
                #print len(r.seq)
                start, end = coord[name]
                start = int(start) - padding
                end = int(end) + padding
                rc = False
                if start > end:
                    start, end = end, start
                    rc = True
                if rc:
                    seq = r.seq[start-1:end].reverse_complement()
                else:
                    seq = r.seq[start-1:end]
                extractedSegs["%s:%s-%s"%(name,start,end)] = seq
    f.close()

    return extractedSegs    
    

if __name__ == "__main__":
    if len(argv) <> 4:
        os.sys.exit(__doc__)

    queryFile = argv[1]
    dbFile = argv[2]
    padding = int(argv[3])

    bloFname = looseBLAST(queryFile, dbFile)

    coord = getCoordinatesFromBlo(bloFname, padding)
    #print coord
    
    extractedSegs = getSeqByCoord(dbFile, coord, padding)
    #print extractedSegs
    for s in extractedSegs:
        print ">%s\n%s"%(s,extractedSegs[s])


