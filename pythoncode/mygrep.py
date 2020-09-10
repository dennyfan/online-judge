#!/usr/bin/env python3
import sys
numberOfArgs = len(sys.argv)
if numberOfArgs != 3:
    sys.stderr.write('usage: %s pattern inFile\n' %sys.argv[0])
    sys.exit(1)
try:
    fh = open(sys.argv[2], 'r')
except:
    sys.stderr.write('cannot open input file %s\n' %sys.argv[2])
    sys.exit(2)
pattern = sys.argv[1]
for line in fh.readlines():
    if line.find(pattern) >= 0:
        print(line, end='')
fh.close()
