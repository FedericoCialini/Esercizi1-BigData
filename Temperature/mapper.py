#!/usr/bin/env python
"""mapper.py"""
import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    year = line[15:19]
    if line[87] == "+":
        temperature = line[88:92]
        print('%s\t%s' % (year, temperature))
    elif line[87] == "-":
        temperature = line[87:92]
        print('%s\t%s' % (year, temperature))
