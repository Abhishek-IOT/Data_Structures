try:
    test=int(input())
    for i in range(test):
        l,m,h=list(map(int,input().split(' ')))
        ans=m+(100-l)*h
        print(ans*10)

except:
    pass
