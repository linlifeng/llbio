#!/usr/bin/python

'''
1. fname
2. row col
3. col col
4. data col
5. function
'''


import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sys import exit, argv

try:
    fname = argv[1]
    row = int(argv[2]) - 1
    col = int(argv[3]) - 1
    data = int(argv[4]) - 1
    func = argv[5]
except:
    exit(__doc__)


df = pd.read_csv(fname, sep='\t')
#plt.scatter(x=df[c1], y=df[c2], s=.5)
#plt.savefig('out_png', dpi=150)

headers = list(df)

pivot = pd.pivot_table(df, values=headers[data], columns=headers[col], index=headers[row], aggfunc='mean')
pivot.to_csv("pivot.tab", sep='\t', encoding='utf-8')

