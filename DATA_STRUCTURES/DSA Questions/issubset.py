def subset(arr,w):
    l=len(arr)
    dp=[[0 for i in range(w+1)]for j in range(l+1)]
    for i in range(l+1):
        for j in range(w+1):
            if i==0:
                dp[i][j]=0
            if j==0:
                dp[i][j]=1
    for i in range(1,l+1):
        for j in range(1,w+1):
            if arr[i-1]<=j:
                dp[i][j]=(dp[i-1][j-arr[i-1]] or dp[i-1][j])
            else:
                dp[i][j]=dp[i-1][j]


    print(dp)
    return dp[l][w]

if __name__ == '__main__':
    arr=[3, 34, 4, 12, 5, 2]
    w=30
    m=subset(arr,w)
    if m==1:
        print("Yes found")
    else:
        print('Not found baby')