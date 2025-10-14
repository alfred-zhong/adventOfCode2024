
left, right = [], []
with open("input.txt") as f:
    for line in f:
        ss = line.strip().split()
        left.append(int(ss[0]))
        right.append(int(ss[1]))

left.sort()
right.sort()

distance = 0
for i in range(len(left)):
    distance += abs(left[i] - right[i])

print(distance)
