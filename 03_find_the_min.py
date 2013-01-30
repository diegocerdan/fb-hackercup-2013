#!/usr/bin/python
from __future__ import print_function
from collections import deque
from collections import Counter
import heapq
import sys

file = open(str(sys.argv[1]), 'r')
lines = file.readlines()

for j in range(1, len(lines), 2):
    n, k = [int(x) for x in lines[j].split()]
    a, b, c, r = [int(x) for x in lines[j+1].split()]

    m = deque([a])
    for i in range(1, k):
        m.append((b * m[-1] + c) % r)

    used = [False] * (k+1)
    for i in m:
        if i < k:
            used[i] = True

    non_used = []
    for i, value in enumerate(used):
        if not used[i]:
            non_used.append(i)
    heapq.heapify(non_used)


    counter = Counter(m)

    final = ((n+1)%(k+1))

    for i in range(final):
        min = heapq.heappop(non_used)

        m.append(min)
        counter[min] += 1

        discarded = m.popleft()
        counter[discarded] -= 1

        if discarded < k and counter[discarded] == 0:
            heapq.heappush(non_used, discarded)

    print('Case #', (j//2) + 1, ': ', m[-1], sep='')
