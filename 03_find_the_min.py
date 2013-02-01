#!/usr/bin/python
from __future__ import print_function
from collections import deque
from collections import Counter
import heapq
import sys

file = open(str(sys.argv[1]), 'r')

cases = int(file.readline())

for case in range(1, cases + 1):
    n, k = [int(x) for x in file.readline().split()]
    a, b, c, r = [int(x) for x in file.readline().split()]

    n = k + (n+1) % (k+1)

    m = deque([a])
    for i in range(1, k):
        m.append((b * m[-1] + c) % r)

    counter = Counter(m)

    missing = [e for e in range(k+1) if not counter[e]]
    heapq.heapify(missing)

    for i in range(k, n):
        min = heapq.heappop(missing)

        m.append(min)
        counter[min] += 1

        discarded = m.popleft()
        counter[discarded] -= 1

        if counter[discarded] == 0:
            heapq.heappush(missing, discarded)

    print('Case #', case, ': ', m[-1], sep='')