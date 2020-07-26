#!/usr/bin/python

'''
download all NCBI sequences that match a certain keyword

argument
1. keyword
2. starting batch number (optional, default start with 1)
3. return type (fasta/gb, optional, default use fasta)
usage example:

~ "Mycobacterium tuberculosis complex[orgn]" 21 gb

this will download starting all sequences within that taxon, starting with the 22nd batch (sequences 210,000)
'''
from Bio import SeqIO, Entrez
from sys import argv, exit
import os

def ncbiDownload(query, bStart, db):
    if db == 'fasta':
        suffix = 'fsa'
    elif db == 'gb':
        suffix = 'gb'
    else:
        exit("unrecognized rettype: %s"%db)

    outfName = "%s_ncbi_all.%s"%(query.replace('[orgn]','').replace(' ','_'), suffix)
    append = 'y'
    if os.path.isfile(outfName):
        print "--[WARNING] %s already downloaded (file name: %s). Skipping to next..."%(query, outfName)
        append = ''
        while not append.rstrip().lower() == 'y' and not append.rstrip().lower() == 'n':
            append = raw_input("Are you appending to an unfinished downlowd? (y/n)")
    if append.rstrip().lower() == 'n':
        exit('--[STOPPED] File exists')
    else:
        #Entrez.email = 'lifeng.lin@lifetech.com'
        Entrez.email = 'linlifeng@gmail.com'
        handle = Entrez.esearch(db='nucleotide', term = query, retmax = 10000)
        record = Entrez.read(handle)
        count = record['Count']
        bnum = 0
        if int(count) > 10000:
            print "[WARNING]there are %s records for this download. Exceeded the maximum download limit of 10k. Breaking into batches."%(count)
            bnum = int(count)/10000 + 1

        if bnum == 0:
            print "Downloading %s records for %s"%(count, query)
            gi_list = record['IdList']
            gi_str = ",".join(gi_list)
            '''
            handle = Entrez.efetch(db='nuccore', id = gi_str, rettype = db, retmode='text')
            results = handle.read()
            outfile = open(outfName,'w')
            outfile.write(results)
            outfile.close()
            '''
        else:
            for i in range(bStart - 1, bnum):
                print "---downloading batch %s"%(i+1),
                handle = Entrez.esearch(db='nucleotide', term = query, retmax = 10000, retstart = i*10000)
                record = Entrez.read(handle)    
                gi_list = record['IdList']
                print len(gi_list), "sequences"
                gi_str = ",".join(gi_list)
                '''
                handle = Entrez.efetch(db='nuccore', id = gi_str, rettype = db, retmode='text')
                results = handle.read()
                outfile = open(outfName,'a')
                outfile.write(results)
                outfile.close()
                '''
        return gi_str   

def main():
    try:
        query = argv[1]
        bStart = int(argv[2])
        db = argv[3]
    except:
        if len(argv) == 2:
            print "[NOTICE]--Using default type as fasta and start batch as 1"
            bStart = 1
            db = 'fasta'
        else: 
            exit(__doc__)
    '''
    if len(argv) == 1 or len(argv) > 3:
        exit(__doc__)
    else:
        bStart = int(argv[2])
    query = argv[1]
    '''

    if os.path.isfile(query):
        f = open(query, 'r')
        for l in f:
            ncbiDownload("%s"%l.rstrip(), bStart, db)
    else:
        gis = ncbiDownload(query, bStart, db)
    o = open("giNumbers.txt", 'w')
    '''
    for gi in gis.split(','):
        o.write(gi + '\n')
    '''
    o.write(gis)
    o.close()

if __name__ == '__main__':
    main()    
