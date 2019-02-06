#!/usr/bin/env python

'''
1. primer in tab format.
2. allow mismatch (y/n)
    if mismatches are allowed, then primers with only a single bp mismatch > 10bp from extension end are considered replaceable
3. forward tag sequence(optional)
4. reverse tag sequence(optional)
    * sometimes primers contain adaptor sequences that needs to be excluded from deduplicaton.
    if specified, these tags will be removed first and added on later to the unique primers.

'''

from sys import argv, exit
from os import system
import networkx as nx
from collections import defaultdict

try:
    fname = argv[1]
    allowMM = argv[2]
except:
    exit(__doc__)

if len(argv) > 3:
    ftag = argv[3]
    rtag = argv[4]
else:
    ftag = ''
    rtag = ''

mm = False
if allowMM.upper() in ['Y','YES']:
    mm = True
if not allowMM.upper() in ['N','NO','Y','YES']:
    exit("allow mm must be yes or no, or y or n")

def mmCnt(p1, p2):
    '''
    p1 and p2 are identical length DNA sequences
    '''
    diff = 0
    inLast10 = False
    for i in range(len(p1)):
        if not p1[i] == p2[i]:
            diff += 1
            if i > len(p1) - 10:
                inLast10 = True
    return diff, inLast10

def comparePrimers(new, existing, mm):
    if len(new) == len(existing):
        diffCnt, inLast10 = mmCnt(new, existing)
        if diffCnt == 0:
            return "identical"
        elif diffCnt < 2 and not inLast10 and mm:
            return "similar"
        else:
            return "different"
    if len(new) < len(existing):
        shortenedExisting = existing[-len(new):]
        diffCnt, inLast10 = mmCnt(new, shortenedExisting)
        if  diffCnt == 0:
            return "replace"
        elif diffCnt < 2 and not inLast10 and mm:
            return "replace"
        else:
            return "different"
    return 'different'


#build digraph
G = nx.DiGraph()

f = open(fname, 'r')
primerWeight = defaultdict(int)
primerNames = defaultdict(list)
for l in f:
    segs = l.rstrip().split('\t')
    seqName, seq = segs
    primerWeight[seq] += 1
    primerNames[seq].append(seqName)
f.close()

for p in primerWeight:
    G.add_node(p, weight=primerWeight[p])

relationships = {}
for p in primerWeight:
    for q in primerWeight:
        if p == q:
            continue
        pgsp = p
        qgsp = q

        if ftag == p[:len(ftag)]:
            pgsp = p[len(ftag):]
            #gsprimer = primerSeq.replace(ftag,'')
        if rtag == p[:len(rtag)]:
            pgsp = p[len(rtag):]
            #gsprimer = primerSeq.replace(rtag,'')

        if ftag == q[:len(ftag)]:
            qgsp = q[len(ftag):]
            #gsprimer = primerSeq.replace(ftag,'')
        if rtag == q[:len(rtag)]:
            qgsp = q[len(rtag):]
            #gsprimer = primerSeq.replace(rtag,'')


        relationship = comparePrimers(pgsp,qgsp, mm)
        relationships[p+q] = relationship
        if relationship in ['identical', 'similar']: 
            G.add_edge(p, q)
            G.add_edge(q, p)
        if relationship == 'replace':
            G.add_edge(p, q)

keepSet = []
logf = open(fname+'dedup.log.txt','w')
while len(set(keepSet)) < len(G.nodes()):
    maxout = 0
    rmWeight = 0
    rmNode = False
    for n in G.nodes():
        weight = primerWeight[str(n)]
        ind = G.in_degree(n)
        ond = G.out_degree(n)
        if ind == 0:
            keepSet.append(str(n))
        if ond > maxout:
            maxout = ond
            rmWeight = weight
            rmNode = n
        elif ond == maxout and weight < rmWeight:
            rmWeight = weight
            rmNode = n

    if not rmNode:
        break
    keepSet.append(str(rmNode))
    for pair in G.out_edges(rmNode):
        p, q = pair
        relationship = relationships[p+q]
        logf.write("%s\tcoveredBy\t%s\t%s\n"%(q, p,relationship))
        G.remove_node(q)    
logf.close()

for primer in set(keepSet):
    print("%s\t%s"%(primerNames[primer][0],primer))
