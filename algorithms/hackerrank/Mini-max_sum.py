#!/bin/python3

import sys

arr = list(map(int, input().strip().split(' ')))

def min_max(arr):
    minimum = 0
    maximum = 0
    arr.sort()
    for i in arr[0:4]:
        minimum += i
    for i in arr[-1:-5:-1]:
        maximum += i
    return [minimum, maximum]

result = min_max(arr)

print(result)
