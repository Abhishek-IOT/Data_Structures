def knapsack(w,val,wt,n):
    dp=[[0 for i in range(wt+1)]for j in range(n+1)]
    for i in range(n+1):
        for j in range(wt+1):
            if i==0 or j==0:
                dp[i][j]=0
    for i in range(n+1):
        for j in range(wt+1):
            if w[i-1]<=j:
                dp[i][j]=max(val[i-1]+dp[i-1][j-w[i-1]],dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]
    printMat(dp,n,wt)
    return dp[n][wt]
def printMat(dp,n,wt):
    for i in range(n+1):
        print("[",end=" ")
        for j in range(wt+1):
            print(dp[i][j],end=",")
        print("]")

if __name__ == '__main__':
    w=[1,3,5,6]
    n=4
    wt=5
    val=[1,4,2,3]
    m=knapsack(w,val,wt,n)
    print("Maximum Profit=",m)
