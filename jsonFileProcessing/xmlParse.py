#!/usr/bin/env python
'''
1. file name
2. column for the xml 
'''
from sys import argv
from bs4 import BeautifulSoup

try:
    f   = open(argv[1])
    col = int(argv[2]) - 1
except:
    exit(__doc__)


for l in f:
    segs = l.rstrip().split("\t")
    xml  = segs[col]
    soup  = BeautifulSoup(xml, 'xml')
    try:
        soup  = BeautifulSoup(xml, 'xml')
    except:
        exit("Cannot parse xml %s"%xml)

    #assayID  = soup.find_all('Extrinsic', {'name' :'UniqueAssayID'})
    #print soup.keys()
    #seqName  = soup.ItemDetail.Extrinsic.OligoMixSpecification.Oligos.MixItem.OligoSpecification.find_all('Name')
    mixItems  = soup.ItemDetail.Extrinsic.OligoMixSpecification.Oligos.find_all('MixItem')
    #seq      = soup.ItemDetail.Extrinsic.OligoMixSpecification.Oligos.MixItem.OligoSpecification.SequenceToManufacture.contents
    assayID = soup.ItemDetail.Extrinsic.find_all('Extrinsic', {'name': 'UniqueAssayID'})
    

    for i in range(len(mixItems)):    
        print assayID[0], mixItems[i].OligoSpecification.Name.contents[0], mixItems[i].OligoSpecification.SequenceToManufacture.contents[0]
