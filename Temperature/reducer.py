#!/usr/bin/env python
"""reducer.py"""
from operator import itemgetter
import sys
year_list = []
h = {}
for line in sys.stdin:
    line = line.strip()
    year, temperature = line.split('\t')
    h[year] = h.get(year,[]) + [temperature]
    if not(year in year_list):
        year_list.append(year)
for year in year_list:
    maxTemperature = max(h[year])
    print('%s\t%s' % (year, float(maxTemperature) / 10))
print('%s\t%s' % (year, float(maxTemperature) / 10))
