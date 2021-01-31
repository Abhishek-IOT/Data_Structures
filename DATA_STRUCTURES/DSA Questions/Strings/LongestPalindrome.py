"""
Longest Palindromic Subsequence
Logic=We will use LCS with a little difference ,with a little difference instead of b we will send the reverse of a.
"""
def longestPalindromic(a,b,n):
    dp=[[0 for i in range(n+1)]for j in range(n+1)]
    for i in range(n+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
    for i in range(1,n+1):
        for j in range(1,n+1):
            if a[i-1]==b[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[n][n]
if __name__ == '__main__':
    a="GEEKSFORGEEKS"
    n=len(a)
    rev=""
    for i in range(n-1,-1,-1):
        rev=rev+a[i]
    print(rev)
    m=longestPalindromic(a,rev,n)
    print(m)
