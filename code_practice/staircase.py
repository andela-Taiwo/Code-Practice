#!/bin/python

import sys


n = int(raw_input().strip())
j = n

for i in range(1,n+1):
    print(" "*(j-1))+("#"*i)

    j -=1
