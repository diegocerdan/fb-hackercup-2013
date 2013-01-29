#!/usr/bin/python
from __future__ import print_function
import sys, collections

MAX_LETTER_BEAUTY = ord('z') - ord('a') + 1

file = open(str(sys.argv[1]), 'r')
lines = file.readlines()

for i, line in enumerate(lines[1:]):
  result = 0
  counts = collections.Counter(line.lower()).most_common()

  max = MAX_LETTER_BEAUTY

  for char, times in counts:
    if char >= 'a' and char <= 'z':
      result += times * max
      max -= 1

  print('Case #',i+1, ': ', result, sep='')