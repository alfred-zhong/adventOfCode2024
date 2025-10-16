import sys, os
from typing import List
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'common')))

from util import select_input_file
import math

def has_even_digits(num):
    if num == 0:
        return False, 1  # 0有1位，这里按1位处理
    # 处理负数
    num = abs(num)
    # 计算位数：log10(num) + 1 的整数部分
    digits = int(math.log10(num)) + 1
    return digits % 2 == 0, digits

from functools import lru_cache

@lru_cache(maxsize=1024*1024)
def blink(num: int, cnt: int) -> int:
    if cnt == 0:
        return 1

    even, digits = has_even_digits(num)
    if num == 0:
        return blink(1, cnt -1)
    elif even:
        return blink(num // (10 ** (digits // 2)), cnt - 1) + blink(num % (10 ** (digits // 2)), cnt - 1)
    else:
        return blink(num*2024, cnt - 1)

        
with open(select_input_file(['example.txt', 'example1.txt', 'input.txt'])) as f:
    nums = [int(x) for x in f.readline().strip().split()]

cnt = 0
for num in nums:
    cnt += blink(num, 75)
print(f'count: {cnt}')
