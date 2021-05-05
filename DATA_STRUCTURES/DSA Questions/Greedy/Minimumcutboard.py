def mincost(x,y,m,n):
    res=0
    x.sort(reverse=True)
    y.sort(reverse=True)
    h=1
    v=1
    i,j=0,0
    while(i<m and j<n):
        if x[i]<y[j]:
            res+=y[j]*h
            v=v+1
            j=j+1
        else:
            res+=x[i]*v
            h=h+1
            i=i+1
    print(res)
    total=0
    while i<m:
        total+=x[i]
        i=i+1
    res+=total*v
    total=0
    while(j<n):
        total+=y[j]
        j=j+1
    res+=total*h
    return res
m = 6; n = 4
X = [2, 1, 3, 1, 4]
Y = [4, 1, 2]
yup=mincost(X,Y,m-1,n-1)
print(yup)
