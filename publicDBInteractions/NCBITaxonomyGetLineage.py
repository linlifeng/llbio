#!/usr/bin/python

from Bio import Entrez

def getLineageByID(tID):
    '''
    currently search one level up and two level down.
    could potentially be transformed into recursive function that search until found.
    '''
    import cx_Oracle
    con = cx_Oracle.connect('bactdev/bactdev@ora2.itw:1521/BACTRACK')
    #print con.version
    cursor = con.cursor()
    
    
    tid = tID
    fullList = []
    shortLineage = {}
    shortLineage['species'] = (0, 'na')
    shortLineage['genus'] = (0, 'na')
    shortLineage['family'] = (0, 'na')
    shortLineage['order'] = (0, 'na')

    sql = 'select * from TAXONOMY where TAXON_ID = %s'%tid
    cursor.execute(sql)
    for r in cursor:
        currentRank = r[4]
        currentName = r[2]
    if cursor.rowcount == 0:
        shortLineage['species'] = (0, 'na')
    elif currentRank == 'species':
        shortLineage['species'] = (tid, currentName)

    while not tid == 1:
        sql = 'select * from TAXONOMY where TAXON_ID in \
                (select PARENT_ID from TAXONOMY where TAXON_ID = %s)'%tid #this searches one level up.
        cursor.execute(sql)
        for r in cursor:
            tid = r[0]
            tName = r[2]
            rank = r[4].strip()
            fullList.append((rank,tName))
            if rank == 'species':
                shortLineage['species'] = (tid, tName)
            elif rank == 'genus':
                shortLineage['genus'] = (tid, tName)
            elif rank == 'family':
                shortLineage['family'] = (tid, tName)
            elif rank == 'order':
                shortLineage['order'] = (tid,tName)
            elif rank == 'superkingdom':
                shortLineage['superkingdom'] = (tid,tName)
        if cursor.rowcount == 0:
            break
        #print sql
        #print rank,'\t', tid, '\t', tName
    #for i in shortLineage:
        #print i, shortLineage[i]
    #print fullList
    return shortLineage


def getLineageFromTaxonId(tid):
    # set email
    Entrez.email = "lifeng.lin@lifetech.com"

    # traverse ids
    lineage = {}
    handle = Entrez.efetch(db="taxonomy", id=tid, mode="text", rettype="xml")
    records = Entrez.read(handle)
    for taxon in records:
        taxid = taxon["TaxId"]
        name = taxon["ScientificName"]
        rank = taxon['Rank']
        tids = []
        for t in taxon["LineageEx"]:
            tids.insert(0, t["TaxId"])
        tids.insert(0, taxid)
        #print "%s\t%s\t%s\t%s" % (taxid, name, rank, " ".join(tids))
        lineage[taxid] = tids
            #print taxon.keys()
    return (tid, name, rank, tids)


def getLineageFromOrgName(taxName):
    # set email
    Entrez.email = "lifeng.lin@lifetech.com"

    # traverse ids
    lineage = {}
    tids = []
    handle = Entrez.esearch(db="taxonomy", term=taxName, mode="text", rettype="xml")
    records = Entrez.read(handle)['IdList']
    for taxon in records:
        tids.append(taxon)
    if len(tids) > 1:
        exit("[Oops]..the keyword %s is ambiguos and correspond to more than one taxonomy ID\n"%taxName)
    else:
        return getLineageFromTaxonId(tids[0])
    

def main():
    from sys import argv,exit
    if len(argv) <> 2:
        exit(__doc__)
    print getLineageByID(argv[1])

if __name__ == "__main__":
    main()
