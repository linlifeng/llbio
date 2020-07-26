#!/usr/bin/python
'''
usage:

~ inputfile(org list)
'''


from Bio import SeqIO, Entrez
from sys import argv, exit
import os

def ncbiCount(query):
    Entrez.email = 'lifeng.lin@lifetech.com'
    handle = Entrez.esearch(db='nucleotide', term = query, retmax=1000000)
    record = Entrez.read(handle)
    count = record['Count']
    return count
'''
if int(count) > 1000000:
    print "[WARNING]there are %s records for this download. Only the top 1 million entries will be returned."%(count)
else:
    print "Downloading %s records for %s"%(count, query)

gi_list = record['IdList']
gi_str = ",".join(gi_list)
handle = Entrez.efetch(db='nuccore', id = gi_str, rettype = 'fasta', retmode='text')
results = handle.read()
outfile = open(outName,'w')
outfile.write(results)
'''

def main():
    if len(argv) <> 2:
        exit(__doc__)
    query = argv[1]
    if os.path.isfile(query):
        f = open(query, 'r')
        for l in f:
            count = ncbiCount("%s"%l.rstrip())
            print "%s\t%s"%(l.rstrip(), count)
    else:
        count = ncbiCount(query)
        print "%s\t%s"%(query, count)
if __name__ == '__main__':
    main()    
