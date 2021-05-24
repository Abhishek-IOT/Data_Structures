def findsmall(m,s):
    res=[0 for i in range(m+1)]
    s=s-1
    for i in range(m-1,0,-1):
        if s>9:
            res[i]=9
            s-=9
        else:
            res[i]=s
            s=0
    res[0]=s+1
    for i in range(m):
        print(res[i],end=' ')

m=3
s=20
q=findsmall(m,s)
