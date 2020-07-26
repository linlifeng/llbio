#!/usr/bin/python
'''
1. taxonID
'''

def getTaxonByID(tid):
    import cx_Oracle
    con = cx_Oracle.connect('bactdev/bactdev@ora2.itw:1521/BACTRACK')
    #print con.version
    cursor = con.cursor()
    sql = 'select * from TAXONOMY where TAXON_ID = \'%s\''%tid
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
    if spIDList == []:
        return (tid, 'ID not found', 'ID not found')
    return (spIDList[0], spNameList[0], rankList[0])

def main():
    from sys import argv,exit
    if len(argv) == 1:
        exit(__doc__)
    taxonArray = getTaxonByID(argv[1])
    print "%s\t%s\t%s"%(taxonArray[0], taxonArray[1], taxonArray[2])
        

if __name__ == "__main__":
    main()
