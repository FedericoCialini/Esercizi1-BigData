##!/usr/bin/env python
"""reducer.py"""
import sys
h={}
for line in sys.stdin:
    line = line.split(" ")
    word = line[0]
    lineNumber=line[1]
    h[word] = h.get(word,[]) + [int(lineNumber)]
for word in sorted(h.keys()):
    print ('%s\t%s' % (word,h.get(word)))