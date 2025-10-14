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
do = True
for section in sections:
    matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", section)
    # print(matches)

    section_sum = 0
    do_count, donot_count = 0, 0
    for match in matches:
        if match.startswith("mul") and do:
            section_sum += calc(match)
        elif match == "do()":
            do = True
            do_count += 1
        elif match == "don't()":
            do = False
            donot_count += 1

    print(section_sum)
    print(f"do: {do_count}, don't: {donot_count}")
    result += section_sum

print(f'result: {result}')
