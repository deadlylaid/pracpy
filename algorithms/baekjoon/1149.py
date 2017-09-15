a=int(input())
list_a = [[0,0,0]]
dp = [ [0,0,0] for _ in range(a+1) ]
for i in range(a):
    list_a.append(list(map(int, input().split())))

for i in range(1, a+1):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + list_a[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + list_a[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + list_a[i][2]

print(min(dp[a][0], dp[a][1], dp[a][2]))
