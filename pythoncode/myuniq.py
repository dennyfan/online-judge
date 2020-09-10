#!/usr/bin/env python3
import sys
numberOfArgs = len(sys.argv)
if numberOfArgs != 2:
    sys.stderr.write('usage: %s inputFile\n' %sys.argv[0])
    sys.exit(1)
try:
    fh = open(sys.argv[1], 'r')
except:
    sys.stderr.write('cannot open input file %s\n' %sys.argv[1])
    sys.exit(2)
previousline = ''
for line in fh.readlines():
    if line != previousline:
        print(line, end='')#plus [end] here to avoid [print] to 開始新的一行
    previousline = line
fh.close()
