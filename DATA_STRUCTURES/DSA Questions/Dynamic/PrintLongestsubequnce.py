def printLcs(x,y,m,n,dp):
    i=m
    j=n
    s=""
    while(i>0 and j>0):
        if x[i-1]==y[j-1]:
            s=s+x[i-1]
            i-=1
            j-=1
        else:
            if dp[i][j-1]>dp[i-1][j]:
                j-=1
            else:
                i-=1
    return s
def printmat(mat,row,col):
    for i in range(row):
        print("[",end=" ")
        for j in range(col):
            print(mat[i][j],end=" ")
        print("]")
def longestsubseq(x,y,m,n):
    dp=[[0 for i in range(n+1)]for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                dp[i][j]=0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1]==y[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    yoyo=printLcs(x,y,m,n,dp)
    return yoyo

if __name__ == '__main__':
    a='acbcf'
    b='abcdaf'
    n=len(a)
    m=len(b)
    y=longestsubseq(a,b,n,m)
    print(y)
    for i in range(len(y)-1,-1,-1):
        print(y[i],end="")

    # printmat(y,n+1,m+1)