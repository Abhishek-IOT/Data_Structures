"""
arr=[1,2,3,5]
    w=8
    Then there will be two subset formed={1,2,5} and {3,5}.We have to return the count of subsets formed.
    We will use D.P for checking the knapsaxk problem.
"""
def printmat(mat,row,col):
    for i in range(row):
        print("[ ",end=" ")
        for j in range(col):
            print(mat[i][j],end=" ")
        print(" ]")
def countofsubsets(arr,w):
    n=len(arr)
    dp=[[0for i in range(w+1)]for j in range(n+1)]
    for i in range(n+1):
        for j in range(w+1):
            if i==0:
                dp[i][j]=0
            if j==0:
                dp[i][j]=1
    for i in range(1,n+1):
        for j in range(1,w+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j]+dp[i-1][j-arr[i-1]]
            else:
                dp[i][j]=dp[i-1][j]
    return dp[n][w]
if __name__ == '__main__':
    arr=[1,2,3,5]
    w=8
    m=countofsubsets(arr,w)
    # printmat(m,len(arr)+1,w+1)
    print(m)
