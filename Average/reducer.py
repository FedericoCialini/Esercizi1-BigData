#!/usr/bin/env python
"""reducer.py"""
import sys
h={}
for line in sys.stdin:
    line = line.strip()
    line = line.split("\t")
    h[line[0]] = h.get(line[0],[]) + [int(line[1])]

for c in sorted(h.keys()):
    print (c + " " + str(sum(h.get(c))/len(h.get(c))))