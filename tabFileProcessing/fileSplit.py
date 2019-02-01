#!/usr/bin/env python

'''
convert large file into small subsets

1. file name
2. fragment size
'''

from sys import argv, exit
from os import path, system

try:
    fname = argv[1]
    fragSize = int(argv[2])
except:
    exit(__doc__)


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


fsize = file_len(fname)
fragNum = fsize/fragSize
if not fsize % fragSize == 0:
    fragNum += 1

if fragNum >= 100:
    decision = raw_input("you are about to generate a lot of files (%s)! continue? (y/n)"%fragNum)
    if not decision.upper() == 'Y':
        exit("[STOPPED] user decided that there are too many fragments.")


currentLine = 0
remainingLines = fsize - currentLine

i = 0
system("cp %s fragTemp.temp"%fname)
while remainingLines > 0:
    i += 1
    currentLine = i * fragSize
    remainingLines = fsize - currentLine
    ofname = fname + '.frag%s'%i
    system("head -n %s fragTemp.temp > %s"%(fragSize, ofname))
    system("tail -n %s %s > fragTemp.temp"%(remainingLines, fname))

#if file_len("fragTemp.temp") > 0:
#    system("mv fragTemp.temp %s"%(fname + '.frag%s'%(i+1)))
#else:
system("rm fragTemp.temp")
