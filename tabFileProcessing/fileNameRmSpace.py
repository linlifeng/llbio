#!/usr/bin/env python

'''
1. fname
'''

from sys import argv
from os import system

try:
    fname = argv[1]
except:
    exit(__doc__)

system("mv %s %s"%(fname.replace(' ','\ '), fname.replace(' ', '_')))

