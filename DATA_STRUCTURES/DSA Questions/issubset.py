"""
Subset Sum Problem | DP-25
Difficulty Level : Medium
 Last Updated : 09 Nov, 2020

Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

Example:

Input: set[] = {3, 34, 4, 12, 5, 2}, sum = 9
Output: True
There is a subset (4, 5) with sum 9.
Logic =We are using the D.P Top down approach for the problem.(It is 0/1 knapsack problem

"""
def sumsubset(arr,cap,n):
    dp = ([[False for i in range(sum + 1)]
           for i in range(n + 1)])
    for i in range(n+1):
        for j in range(cap+1):
            if i==0:
                dp[i][j]=False
            if j==0:
                dp[i][j]=True
    for i in range(n+1):
        for j in range(cap+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] =dp[i-1][j]
    return dp[n][cap]
if __name__ == '__main__':
    arr=[3, 34, 4, 12, 5, 2]
    sum=9
    n=len(arr)+1
    net=sum+1
    y=sumsubset(arr,sum,len(arr))
    if y==True:
        print("Yes found")
    else:
        print("No")
