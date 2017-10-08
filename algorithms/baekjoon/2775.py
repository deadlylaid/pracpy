num_of_test_case=int(input())

def dynamic_programing(floor, no):
    dp=[]
    for i in range(floor+1):
        dp.append([0] * (no+1))
        for j in range(no+1):
            if i == 0 or j ==0:
                dp[i][j] = j
            else:
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
    return dp[floor][no]

for i in range(num_of_test_case):
    floor=int(input())
    no=int(input())
    print(dynamic_programing(floor, no))
