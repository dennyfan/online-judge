#!/usr/bin/env python3
import sys
numberofargs = len(sys.argv)
if numberofargs != 2:
    sys.stderr.write(f'usage: {sys.argv[0]} inputFile\n')
    sys.exit(1)
try:
    with open(sys.argv[1], 'r') as fh:
        previousline = ''
        for line in fh.readlines():
            if line != previousline:
                print(line, end='')
            previousline = line
except OSError as err:
    sys.stderr.write(str(err)+ '\n')
    sys.exit(2)
