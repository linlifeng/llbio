#!/usr/bin/python

'''
1. fasta file before strand
'''

def getM8Strand(m8fname):
    '''
    assuming a single query sequence
    '''
    f = open(m8fname, 'r')
    strands = {}
    for l in f:
        segs = l.rstrip().split('\t')
        h,hs,he,score = [segs[i] for i in [1,8,9,11]]
        if h in strands:
            continue
        if he > hs:
            strand = 'plus'
        else:
            strand = 'minus'
#        if h in strands and score < strands[h][1]:
#            continue
#        else:
#            strands[h] = [strand, score]
        strands[h] = [strand, score]


    f.close()
    return strands    

from sys import argv,exit
from Bio import SeqIO
from os import system,path

try:
    fname = argv[1]
    f = open(fname, 'r')
    records = SeqIO.parse(f,'fasta')
except:
    exit(__doc__)

#output files
ref = open("tempRef.fsa",'w')
singletons = open("nohits.fsa",'w')
#get top sequence as reference
for r in records:
    ref.write(">%s\n%s\n"%(r.description, r.seq))
    #if print on screen
    print ">%s\n%s"%(r.description, r.seq)    
    break
ref.close()


#format database for blast
system("formatdb -i %s -p F"%fname)

#run blast
system("blastall -i tempRef.fsa -d %s -p blastn -e 1 -q -2 -F F -m8  -o temp.blo"%fname)

#parse blast (and get strand information)
strands = getM8Strand("temp.blo")

#write out the sequences with unified strand
for r in records:
    if not r.id in strands:
        singletons.write(">%s\n%s\n"%(r.description, r.seq))
        continue

    if strands[r.id][0] == 'plus':
        print ">%s\n%s"%(r.description, r.seq)
    elif strands[r.id][0] == 'minus':
        print ">%s_rc\n%s"%(r.description, r.seq.reverse_complement())
    else:
        exit("strand info not recognized for %s, %s"%(r.id, strands[r.id]))

#write out sequences with no hits


#cleanup
singletons.close()
