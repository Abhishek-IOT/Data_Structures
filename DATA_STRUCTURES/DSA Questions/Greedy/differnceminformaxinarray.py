def mindifference(a,b,n):
    a.sort()
    b.sort()
    s=0
    for i in range(n):
        s+=abs(a[i]-b[i])
    return s
if __name__ == '__main__':
    a=[3, 2, 1]
    b=[1,2,3]
    s=mindifference(a,b,len(a))
    print(s)

