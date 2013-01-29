#!/usr/bin/python
from __future__ import print_function
import sys

file = open(str(sys.argv[1]), 'r')
lines = file.readlines()

for j in range(1, len(lines), 2):
  n, k = [int(x) for x in lines[j].split()]
  a, b, c, r = [int(x) for x in lines[j+1].split()]

  m = [None] * n
  m[0] = a;

  for i in range(1, k):
    m[i] = (b * m[i-1] + c) % r

  for i in range(k, n):
    slice = list(set(m[i-k:i]))
    slice.sort()

    min = k
    for pos, number in enumerate(slice):
      if number != pos:
        min = pos
        break

    m[i] = min

  print('Case #', j/2 + 1, ': ', m[n-1], sep='')