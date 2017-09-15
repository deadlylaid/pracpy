def solution(land):
    len_list = len(land)
    dp = [ [0,0,0,0] for _ in range(len_list) ]
    for i in range(len_list):
        if i == 0:
            dp[0][0] = land[0][0]
            dp[0][1] = land[0][1]
            dp[0][2] = land[0][2]
            dp[0][3] = land[0][3]
        else:
            dp[i][0] = max(dp[i-1][1], dp[i-1][2], dp[i-1][3]) + land[i][0]
            dp[i][1] = max(dp[i-1][0], dp[i-1][2], dp[i-1][3]) + land[i][1]
            dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][3]) + land[i][2]
            dp[i][3] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2]) + land[i][3]
    answer = max(dp[i][0], dp[i][1], dp[i][2], dp[i][3])
    return answer
