from operator import itemgetter

n, c = [int(x) for x in input().split()]
nums = input().split()
dic = {}
for i, num in enumerate(nums):
    if num in dic:
        dic[num][0] += 1
    else:
        dic[num] = [1, -i]

res = []
for key, val in sorted(dic.items(), key=itemgetter(1), reverse=True):
    res += [key] * val[0]
print(' '.join(res))
