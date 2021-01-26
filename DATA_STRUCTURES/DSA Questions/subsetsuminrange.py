"""
Given a sequence of N (1 ≤ N ≤ 34) numbers S1, ..., SN (-20,000,000 ≤ Si ≤ 20,000,000), determine how many subsets of S
(including the empty one) have a sum between A and B (-500,000,000 ≤ A ≤ B ≤ 500,000,000), inclusive.
Input=We are given an array and we are given a range we have to count the number of
subsets in the given range.
"""

def subsetsum(arr,high):
    n=len(arr)
    dp=[[0 for i in range(high+1)]for j in range(n+1)]
    for i in range(n+1):
        for j in range(high+1):
            if i==0:
                dp[i][j]=0
            if j==0:
                dp[i][j]=1
    for i in range(1,n+1):
        for j in range(1,high+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j-arr[i-1]] + dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][high]

if __name__ == '__main__':
    arr=[1,2,3,4]
    low=2
    high=5
    m=0
    for i in range(low,high):
        m+=subsetsum(arr,i)
        print(m,"M")
    print(m)