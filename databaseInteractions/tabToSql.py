#!/usr/bin/python
'''
1. fname
2. table name
3. a random column name (for skipping duplicates)
'''

from sys import argv

try:
    f = open(argv[1], 'r')
    table = argv[2]
    col   = argv[3]
except:
    exit(__doc__)


for l in f:
    segs = l.rstrip().split("\t")
    reformatted = '"' + '","'.join(segs) + '"'
    reformatted = reformatted.replace('"NULL"', 'NULL')
    print "INSERT INTO %s VALUES (%s) ON DUPLICATE KEY UPDATE %s = %s;" \
        %(table, reformatted, col, col)
f.close()
