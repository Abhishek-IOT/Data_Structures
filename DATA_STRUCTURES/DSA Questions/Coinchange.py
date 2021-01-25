"""
We will be given an coin array and the sum we have to make.We have to return the total no of count of all possible types we can make for the coin arr
Input={1,2,3}
sum=5
O/P=5
1)1+2+3
2)2+3
3)1+1+3
4)1+1+1+2
5)1+1+1+1+1
"""
def coinchage(coin,sum,n):
    dp=[[0 for i in range(sum+1)]for j in range(n+1)]
    for i in range(n+1):
        for j in range(sum+1):
            if i==0:
                dp[i][j]=0
            if j==0:
                dp[i][j]=1
    for i in range(1,n+1):
        for j in range(1,sum+1):
            if coin[i-1]<=j:
                dp[i][j]=dp[i][j-coin[i-1]]+dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][sum]
if __name__ == '__main__':
    arr=[1,2,3]
    sum=5
    n=len(arr)
    m=coinchage(arr,sum,n)
    print(m)
