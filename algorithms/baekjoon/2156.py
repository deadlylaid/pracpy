a=int(input())
b=[int(input()) for _ in range(a)]
dp=[0]*a

def dynamic(dp, b, i, value):
    if i == 0:
        return value
    elif i == 1:
        return b[i-1]+value
    elif i == 2:
        return max(b[i-1]+value, b[i-2]+value)
    else:
        return max(max(dp[:i-1])+value, max(dp[:i-2])+b[i-1]+value)

for i in range(len(b)):
    dp[i] = dynamic(dp, b, i, b[i])

print(max(dp))
