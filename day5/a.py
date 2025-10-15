from typing import List


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

sum = 0
for update in updates:
    if is_update_valid(update, orders):
        # print(update)
        sum += update[len(update) // 2]
print(sum)
