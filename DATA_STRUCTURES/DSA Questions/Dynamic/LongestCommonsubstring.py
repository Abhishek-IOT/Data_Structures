def longestSubsequence(x, y, m, n):
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    # print(dp)
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
    result=0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
                result=max(result,dp[i][j])
            else:
                dp[i][j] = 0
    return result
if __name__ == '__main__':
    a="Abhishek"
    b="TAbhi"
    n=len(a)
    m=len(b)
    y=longestSubsequence(a,b,n,m)
    print(y)