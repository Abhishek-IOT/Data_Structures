def Subsetsum(arr,n,s):
    dp=[[False for i in range(s+1)]for i in range(n+1)]
    for i in range(n+1):
        for j in range(s+1):
            if i==0:
                dp[i][j]=False
            if j==0:
                dp[i][j]=True
    for i in range(1,n+1):
        for j in range(1,s+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j]
    pirt(dp,n,s)
    print(dp[0][1])
    return dp[n][s]
def pirt(Mat,row,col):
    for i in range(row+1):
        print("[",end=" ")
        for j in range(col+1):
            print(Mat[i][j],end=" ")
        print("]")

if __name__ == '__main__':
    arr=[1,2,3]
    s=5
    m=Subsetsum(arr,len(arr),s)
    if m==True:
        print("Yes Found")
    else:
        print("NO ")

