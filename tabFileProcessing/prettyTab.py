#!/usr/bin/env python

'''
1. tab file
2. header (y/n)
'''

from sys import argv, exit
from tabulate import tabulate
from os import system
from fpdf import FPDF

#print(tabulate([['Alice', 24], ['Bob', 19]], headers=['Name', 'Age']))


try:
    fname = argv[1]
    header = argv[2]
except:
    exit(__doc__)


f = open(fname, 'r')
tabs = []
i = 0
for l in f:
    i += 1
    segs = l.rstrip().split('\t')
    if header.upper() == 'Y' and i == 1:
        headers = segs
        continue
    tabs.append(segs)
f.close()

pdf = FPDF()
pdf.add_page()
pdf.set_font('Courier', size=15)


if header.upper() == 'Y':
    print(tabulate(tabs, headers=headers))
    for l in tabulate(tabs, headers=headers).split("\n"):
        pdf.cell(200, 10, txt=l, ln=1, align='L')

else:
    print(tabulate(tabs))
    for l in tabulate(tabs).split("\n"):
        pdf.cell(200, 10, txt=l, ln=1, align='L')




pdf.output("prettyTab.pdf")
