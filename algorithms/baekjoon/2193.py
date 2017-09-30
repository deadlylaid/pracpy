a=int(input())
dp=[0]*(a+1)
for i in range(1, a+1):
    if i == 1 or i == 2:
        dp[i]=1
    else:
        dp[i] = dp[i-1]+dp[i-2]
print(dp[a])
