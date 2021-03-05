#!/usr/bin/env python

'''

usage:

TmCalc.py <DNA sequence>

'''


from Bio.SeqUtils import MeltingTemp as mt
#from Bio.Seq import Seq
from sys import argv, exit

try:
    #myseq = Seq(argv[1])
    myseq = argv[1]
except:
    exit(__doc__)

Tm  = '%0.2f'%mt.Tm_NN(myseq, Na=100, dnac1=900, dnac2=0)
Len = len(myseq)

print("Tm       :   %s"%Tm)
print("length   :   %s"%Len)
# guoying's production code
# fwd_primerTm= float('%0.2f' % mt.Tm_NN(fwd_primer, Na=param['SALTCONC'], dnac1=param['PRIMERCONC'], dnac2=0))
#SALTCONC=100 # in mM.
#PRIMERCONC=900 # in nM.

#print('%0.2f' % mt.Tm_Wallace(myseq))
#print('%0.2f' % mt.Tm_GC(myseq))
#print('%0.2f' % mt.Tm_NN(myseq))
