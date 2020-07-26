#!/usr/bin/python
'''
1. alignment fasta
2. start pos
3. end pos
'''

def fastaAlnCut(alnFname, start, end, rc):
    from Bio import SeqIO

    alnF = open(alnFname,'r')
    records = SeqIO.parse(alnF, 'fasta')

    frags = {}
    for record in records:
        if rc == True:
            cutFrag = record.seq[start:end].reverse_complement()
        else:
            cutFrag = record.seq[start:end]
        frags[record.id] = cutFrag
    alnF.close()

    return frags


if __name__ == '__main__':
    from sys import argv
    if len(argv) <> 4:
        exit(__doc__)
    alnFname = argv[1]
    start = int(argv[2]) - 1
    end = int(argv[3]) - 1

    frags = fastaAlnCut(alnFname, start, end, False)
    for i in frags:
        print "%s\t%s"%(i, frags[i])
