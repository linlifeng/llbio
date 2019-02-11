#!/usr/bin/env python

'''
1. file name
2. column name 1
3. column name 2 

'''


import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sys import exit, argv

try:
    fname = argv[1]
    c1 = argv[2]  
    c2 = argv[3] 
except:
    exit(__doc__)


df = pd.read_csv(fname, sep='\t')
#print df
plt.scatter(x=df[c1], y=df[c2], s=.5)

plt.savefig('out_png', dpi=150)
