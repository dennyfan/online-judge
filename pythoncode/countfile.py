#!/usr/bin/env pyhton3
def countfile(p = '.'):
    import os
    return 1 if not os.path.isdir(p)\
        else sum(map(countfile, os.listdir(p)))

