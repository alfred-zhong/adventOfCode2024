import collections

left, right = [], []
with open("input.txt") as f:
    for line in f:
        ss = line.strip().split()
        left.append(int(ss[0]))
        right.append(int(ss[1]))

counter = collections.Counter(right)

distances = [x * counter.get(x, 0) for x in left]
print(sum(distances))
