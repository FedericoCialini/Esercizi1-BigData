#!/usr/bin/env python
"""mapper.py"""
import sys
from BigramWritable import Bigram

doc = sys.stdin.read()
doc = doc.strip()
doc = doc.split()
for i in range(0, len(doc) - 1):
    bigram = Bigram(doc[i], doc[i + 1])
    print(bigram.tostring() + " " + str(1))