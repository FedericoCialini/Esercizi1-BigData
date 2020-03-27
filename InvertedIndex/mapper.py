#!/usr/bin/env python
"""mapper.py"""
import sys
for line in sys.stdin:
    doc = line.strip()
    doc = line.split()
    for i in range(1,len(doc)):
        word = doc[i]
        print (word + " " + doc[0])