def countsubsets(arr,s1):
    n=len(arr)
    dp=[[False for i in range(s1+1)]for j in range(n+1)]
    for i in range(n+1):
        for j in range(s1+1):
            if i==0:
                dp[i][j]=False
            if j==0:
                dp[i][j]=True
    for i in range(1,n+1):
        for j in range(1,s1+1):
            if arr[i-1]<=j:
                dp[i][j]=dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i-1][j]
    return dp[n][s1]
def minimumdiff(arr,sum1):
    s=countsubsets(arr,sum1)
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
    diff=10
    arr=[1,2,5]
    s=sum(arr)
    s1=(s+diff)//2
    m=countsubsets(arr,s1)
    if m==True:
        print("Yes it exist")
    else:
        print("No it does not")