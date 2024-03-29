def knapsack(w,val,wt,n):
    dp=[[-1 for i in range(wt+1) ]for j in range(n+1)]
    if n==0 or wt==0:
        return 0
    if dp[n][wt]!=-1:
        return dp[n][wt]
    if w[n-1]<=wt:
        dp[n][wt]=max(val[n-1]+knapsack(w,val,wt-w[n-1],n-1),knapsack(w,val,wt,n-1))
    else:
        dp[n][wt]=knapsack(w,val,wt,n-1)
    return dp[n][wt]

if __name__ == '__main__':
    w=[1,3,5,6]
    n=4
    wt=5
    val=[1,4,2,3]
    m=knapsack(w,val,wt,n)
    print("Maximum Profit=",m)