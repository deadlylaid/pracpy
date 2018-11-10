insert_number = int(input())
insert_list = [0]
insert_list += list(map(int, input().split()))

dp =  [0]*(insert_number+1)

result = -1001

for i in range(1, insert_number+1):
    dp[i] = max(dp[i-1]+insert_list[i], insert_list[i])
    result = max(dp[i], result)
print(result)
