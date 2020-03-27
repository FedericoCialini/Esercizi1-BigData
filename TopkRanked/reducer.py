#!/usr/bin/env python
"""reducer.py"""
import sys
h={}
for line in sys.stdin:
    article,count=line.strip().split('\t')
    h[article] = h.get(article,0) + int(count)
    sorted(h.values(), reverse=True)
for article in h:
    print ('%s\t%s' % (article,h.get(article)))