#!/usr/bin/env python

'''
1. file name (tab delimited)
2. colNumber to filter (1-based)
3. min value (will include in putput)
4. max value (will include in output)

print on screen.

'''
__author__ = 'Lifeng Lin'
__email__ = 'lifeng@paragongenomics.com'


from sys import argv, exit
from os import system

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


try:
	fname = argv[1]
	col = int(argv[2]) - 1
	minVal = float(argv[3])
	maxVal = float(argv[4])
except:
	exit(__doc__)


f = open(fname, 'r')
lf = open("colFilter.log",'w')
skipped = 0
for l in f:
	segs = l.rstrip().split('\t')
	val = segs[col]
	if not is_number(val):
		skipped += 1
		continue
	if float(val) >= minVal and float(val) <= maxVal:
		print l.rstrip()

if not skipped == 0:
	lf.write("%s lines skipped."%skipped)

f.close()
lf.close()
