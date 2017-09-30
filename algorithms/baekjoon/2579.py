a=int(input())
b=[int(input()) for _ in range(a)]
dp = [0] * a

def dynamic(dp, stair, i, value):
    if i == 0:
        return value
    elif i == 1:
        return value + stair[i-1]
    elif i == 2:
        return max(value+stair[i-1], value+stair[i-2])
    else:
        return max(value+stair[i-1]+dp[i-3], value + dp[i-2])

for i in range(a):
    dp[i] = dynamic(dp, b, i, b[i])

print(dp[a-1])
