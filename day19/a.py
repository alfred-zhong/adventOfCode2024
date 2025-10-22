import pygtrie
import heapq
import os
from typing import List


def calc_towels(sequence: str, trie: pygtrie.CharTrie) -> bool:
    n = len(sequence)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(n + 1):
        if dp[i]:
            for p in trie.prefixes(sequence[i:]):
                dp[i + len(p[0])] = True
    return dp[n]


with open(os.sys.argv[1]) as f:
    can_seperate = f.readline().strip().split(', ')
    trie = pygtrie.CharTrie()
    for t in can_seperate:
        trie[t] = True

    f.readline()
    sequences = [line.strip() for line in f.readlines()]

cnt = 0
for sequence in sequences:
    can_seperate = calc_towels(sequence, trie)
    if can_seperate:
        cnt += 1
print(cnt)
