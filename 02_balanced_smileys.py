#!/usr/bin/python
from __future__ import print_function
import sys

file = open(str(sys.argv[1]), 'r')
lines = file.readlines()

for i, line in enumerate(lines[1:]):
  balanced = True
  last_char = None

  smiley_faces = 0
  frowney_faces = 0

  open_parenthesis = 0

  for char in line:
    if char != ' ' and char != ':' and char != '(' and char != ')' and char < 'a' and char > 'z' and char != '\n':
      balanced = False
      break;

    if char == '(':
      open_parenthesis += 1
      if last_char == ':':
        frowney_faces += 1

    if char == ')':
      open_parenthesis -= 1
      if last_char == ':':
          smiley_faces += 1

    if open_parenthesis < 0:
      if - open_parenthesis > smiley_faces:
        balanced = False
        break

    last_char = char

  if open_parenthesis > frowney_faces:
    balanced = False

  if balanced:
    print('Case #',i+1, ': YES')
  else:
    print('Case #',i+1, ': NO')

