"""
Minimum sum partition
Hard Accuracy: 31.01% Submissions: 6954 Points: 8
Given an integer array arr of size N, the task is to divide it into two sets S1
and S2 such that the absolute difference between their sums is minimum and find the minimum difference.
It is just Like subset problem just make the dp table of subset problem and then have the last row of the matrix in array
Have all the index where True till of half of the last of the array and then in it have the min value for difference.
"""
def subset(arr,sum):
    l=len(arr)
    dp=[[False for i in range(sum+1)]for j in range(l+1)]
    for i in range(l+1):
        for j in range(sum+1):
            if i==0:
                dp[i][j]=False
            if j==0:
                dp[i][j]=True
    for i in range(l+1):
        for j in range(sum+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[-1]
def minimumdiff(arr,sum1):
    s=subset(arr,sum1)
    print(s)
    index=[]
    for i in range(len(s)//2):
        if s[i]==True:
            index.append(i)
    print(index)
    max=100000
    for i in range(len(index)):
        max=min(max,sum1-2*index[i])
    return max

if __name__ == '__main__':
    arr=[ 1,4]
    s=sum(arr)
    m=minimumdiff(arr,s)
    print(m)
