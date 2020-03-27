#!/usr/bin/env python
"""reducer.py"""
import sys

if __name__ == '__main__':
    k = sys.argv[1]
    k = int(k)

lines = sys.stdin.readlines()
if k < len(lines):
    for i in range(0, k):
        print(lines[i])
else:
    for i in range(0, len(lines)):
        print(lines[i])
