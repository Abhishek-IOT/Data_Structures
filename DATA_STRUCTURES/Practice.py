def isterm(a,d,x):
    if d==0:
        return x==a
    return ((x-a)%d==0 and int((x-a)/d)>=0)

try:
    test=int(input())
    for i in range(test):
        n,x,k=list(map(int,input().split(' ')))
        n=n+1
        if x%k==0 or isterm(x,k,n):
            print("Yes")
        else:
            print("No")

except:
    pass
