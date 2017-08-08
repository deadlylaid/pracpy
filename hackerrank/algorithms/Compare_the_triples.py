#!/bin/python3

import sys

def solve(list_of_alice, list_of_bob):
    result_list = [0, 0]
    for i in range(0, 3):
        if list_of_alice[i] == list_of_bob[i]:
            pass
        elif list_of_alice[i] > list_of_bob[i]:
            # 엘리스 1점
            result_list[0] += 1
        else:
            # 밥 1점
            result_list[1] += 1
    return result_list

list_of_alice = list(map(int, input().split()))
list_of_bob = list(map(int, input().split()))

result = solve(list_of_alice, list_of_bob)

print (" ".join(map(str, result)))
