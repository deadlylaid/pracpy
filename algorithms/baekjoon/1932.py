a=int(input())
b=[]
dp=[]
for i in range(a):
    b.append([int(x) for x in input().split()])
    dp.append([0]*(i+1))

def dinamic_programming(dp, i, j, value):
    if i == 0 and j == 0:
        return b[i][j]
    elif j == 0:
        return dp[i-1][j] + value
    elif i == j:
        return dp[i-1][j-1] + value
    else:
        return max(dp[i-1][j-1], dp[i-1][j]) + value

for i in range(a):
    for j in range(i+1):

        dp[i][j] = dinamic_programming(dp, i, j, b[i][j])

print(max(dp[a-1]))
