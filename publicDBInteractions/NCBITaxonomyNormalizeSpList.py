#!/usr/bin/python
'''
input:
    1. organism list file
    2. output file name
output:
    organism list at species level
    -lower level will be upgraded to species
    -upper level will be expanded to different species
'''

from sys import argv, exit
#from NCBITaxonomyGetLineage import *

if len(argv) == 1:
    exit(__doc__)

def normalizeSp(tID, tRank):
    '''
    currently search one level up and two level down.
    could potentially be transformed into recursive function that search until found.
    '''
    import cx_Oracle
    con = cx_Oracle.connect('bactdev/bactdev@ora2.itw:1521/BACTRACK')
    #print con.version
    cursor = con.cursor()
    if tRank in ['genus', 'subgenus', 'species group', 'species subgroup']:
        sql = 'select * from TAXONOMY where RANK = \'species\' and \
                (PARENT_ID = %s or PARENT_ID in (select TAXON_ID from TAXONOMY where PARENT_ID = %s))'%(tID, tID) #this searches two levels down.
    elif tRank in ['no rank', 'subspecies']:
        sql = 'select * from TAXONOMY where RANK = \'species\' and TAXON_ID in \
                (select PARENT_ID from TAXONOMY where TAXON_ID = %s)'%tID #this searches one level up.
    else:
        sql = None
        return "[ERROR]Unsupported Rank [%s]."%tRank
    cursor.execute(sql)

    spIDList = []
    spNameList = []
    for r in cursor:
        spIDList.append(r[0])
        spNameList.append(r[2])
    con.close()
    return (spIDList, spNameList)


def getTaxonByName(tName):
    from sys import exit
    try:
        import cx_Oracle
    except:
        exit("cx_Oracle import failed")
    try:
        con = cx_Oracle.connect('bactdev/bactdev@ora2.itw:1521/BACTRACK')
    except:
        exit("db connection failed")
    #print con.version
    cursor = con.cursor()
    sql = 'select * from TAXONOMY where ORGANISM = \'%s\''%tName
    cursor.execute(sql)
    #print sql    
    #print cursor
    
    spIDList = []
    spNameList = []
    rankList = []
    for r in cursor:
        #print r[0], r[2], r[4]
        spIDList.append(r[0])
        spNameList.append(r[2])
        rankList.append(r[4])
    con.close()
    return (spIDList[0], spNameList[0], rankList[0])

def getScientificName(tName):
    import cx_Oracle
    con = cx_Oracle.connect('bactdev/bactdev@ora2.itw:1521/BACTRACK')
    #print con.version
    cursor = con.cursor()
    sql = 'select \"NAME\" from TAXONOMY_ALIAS where \"CLASS\" = \'scientific name\' and TAXON_ID in \
            (select TAXON_ID from TAXONOMY_ALIAS where UPPER(\"NAME\") = UPPER(\'%s\'))'%tName
    cursor.execute(sql)
    for r in cursor:
        name = r[0]
    con.close()
    return name    


def main(infname, outfname):
    parentIds = []
    f = open(infname,'r')
    o = open(outfname, 'w')
    e = open("%s.log"%outfname, 'w')
    expand = 'n'
    for l in f:
        #getLineageFromTaxonId(l.rstrip())
        orgKey = l.rstrip().split('\t')[0]
        print "processing %s..."%orgKey
        try:
            tid, tname, trank = getTaxonByName(orgKey)
            #print "[Success!] %s retrieved"%tname
        except:
            try:
                convertedName = getScientificName(orgKey)
                print "[WARNING] %s is not the scientific name. Suggested name: %s."%(orgKey, convertedName)
                e.write("%s\t%s\t%s\t%s\n"%('na', orgKey, 'na', convertedName))
                #print convertedName
                tid, tname, trank = getTaxonByName(convertedName.replace('\'','\'\''))
            except:
                exit("[FAIL] %s cannot be retrieved from Taxonomy database" %orgKey)
        if trank == 'species':
            o.write(str(tid) + '\t' + tname + '\t' + tname + '\n')
        else:
            print "[WARNING] %s is not a species but a %s"%(tname, trank)
            try:
                spIDs, spNames = normalizeSp(tid,trank)
            except:
                exit("[FAIL] %s cannot be processed. Rank: %s"%(tname, trank))            
            for i in range(len(spIDs)):
                o.write(str(spIDs[i]) + '\t' + spNames[i] + '\t' + tname + '\n')
            e.write(str(tid) + '\t' + tname + '\t' + trank + '\t' + str(len(spIDs)) + '\n')
        
    f.close()
    o.close()
    e.close()

if __name__ == "__main__":
    if len(argv) <> 3:
        exit(__doc__)
    main(argv[1], argv[2])


