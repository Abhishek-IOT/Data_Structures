def maxPlatforms(start,end,n):
    start.sort()
    end.sort()
    plat=1
    result=1
    i=1
    j=0
    while(i<n and j<n):
        if start[i]<end[j]:
            plat+=1
            i=i+1
        elif start[i]>=end[j]:
            plat-=1
            j=j+1
        if plat>result:
            result=plat
    return result
if __name__ == '__main__':
    start=[ 900, 940, 950, 1100, 1500, 1800]
    end=[910, 1200, 1120, 1130, 1900, 2000]
    m=maxPlatforms(start,end,len(start))
    print(m)


e