#!/usr/bin/env python
"""reducer.py"""
import sys
from BigramWritable import Bigram

h = {}
for line in sys.stdin:
    line = line.split(" ")
    bigram = Bigram(line[0], line[1])
    h[bigram] = h.get(bigram, 0) + int(line[2])
    print(h)
for b in sorted(h.keys()):
    print(b.tostring() + " " + str(h.get(b)))
