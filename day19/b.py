import pygtrie
import heapq
import os
from typing import List


def count_segmentations(trie, s):
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # 空字符串有 1 种切分方式

    for i in range(1, n + 1):
        # 检查所有可能的前缀 s[j:i]
        for j in range(i):
            prefix = s[j:i]
            if prefix in trie and dp[j] > 0:
                dp[i] += dp[j]

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
    cnt += count_segmentations(trie, sequence)
print(cnt)
