code = input()

def decryption(code):
    dp = [0]*(len(code)+1)
    dp[0]=1
    dp[1]=1
    if int(code[0]) == 0:
        return 0
    else:
        if len(code)==1:
            return dp[1]
        else:
            for i in range(2,len(code)+1):
                if int(code[i-1])>0:
                    dp[i]=dp[i-1]
                if 10<= int(code[i-2]+code[i-1]) <= 26:
                    dp[i]+=dp[i-2]
    return dp[len(code)]%1000000

print(decryption(code))
