from typing import List
import functools

orders = []
updates = []

with open(input("input file name: ")) as f:
    read_order = True
    for line in f:
        if line.strip() == "":
            read_order = False
            continue
        if read_order:
            orders.append(list(map(int, line.strip().split("|"))))
        else:
            updates.append(list(map(int, line.strip().split(","))))

# print(orders)
# print(updates)

def is_update_valid(update: List[int], orders):
    for order in orders:
        if order[0] in update and order[1] in update:
            if update.index(order[0]) > update.index(order[1]):
                return False
    return True

def cmp(x, y):
    if [x, y] in orders:
        # print([x, y])
        return -1
    elif [y, x] in orders:
        return 1
    else:
        return -1

def sort_update(update: List[int], orders):
    return sorted(update, key=functools.cmp_to_key(cmp))

sum = 0
for update in updates:
    if not is_update_valid(update, orders):
        new_update = sort_update(update, orders)
        # print(new_update)
        sum += new_update[len(new_update) // 2]
print(sum)
