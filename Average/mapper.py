#!/usr/bin/env python
"""mapper.py"""
import sys

doc = sys.stdin.read()
doc = doc.strip()
doc = doc.split()
for word in doc:
    print('%s\t%s' % (word[0],str(len(word))))
