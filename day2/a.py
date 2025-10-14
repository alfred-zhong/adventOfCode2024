

from typing import List


def is_safe(report):
    deltas = [report[i] - report[i-1] for i in range (1, len(report))]
    if all(x > 0 for x in deltas) or all(x < 0 for x in deltas):
        if all(abs(x) <= 3 for x in deltas):
            return True
    return False

reports = []
with open("input.txt") as f:
    for line in f:
        reports.append(list(map(int, line.strip().split())))

safe = 0
for report in reports:
    if is_safe(report):
        safe += 1
print(safe)
