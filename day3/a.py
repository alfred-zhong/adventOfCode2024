import re

def calc(mul):
    # print(mul)
    pairs = re.findall(r"mul\((\d+),(\d+)\)", mul)
    return int(pairs[0][0]) * int(pairs[0][1])

sections = []
with open("input.txt") as f:
    for line in f:
        sections.append(line.strip())

result = 0
for section in sections:
    section_sum = 0
    matches = re.findall(r"mul\(\d+,\d+\)", section)
    for match in matches:
        section_sum += calc(match)
    print(section_sum)
    result += section_sum

print(f'result: {result}')
