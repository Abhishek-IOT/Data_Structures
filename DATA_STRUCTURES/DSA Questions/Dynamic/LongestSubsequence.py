"""
Longest Subsequence=
I/P=X="abcde"
    Y="abfce"
    O/P=4(Length of Subsequence=abce
We will use the longestsubsequence and intialize the [row=0][column=0]=0 and then make check from the last if the common then increase the count and
reduce the strings by one and then if it does not match we will make choose one whole string and one string with reduced the length and vice versa
and then choose the maximum in it.
"""
def longestSubsequence(x, y, m, n):
    dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    # print(dp)
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]


if __name__ == '__main__':
    x = 'abcdgh'
    y = 'abedfhr'
    m = len(x)
    n = len(y)
    print(m, n)
    m = longestSubsequence(x, y, m, n)
    print(m)
