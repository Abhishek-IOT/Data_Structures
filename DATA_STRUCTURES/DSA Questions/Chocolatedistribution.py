def findmin(arr,n,m):
    if m==0 and n==0:
        return 0
    if n>m:
        return -1
    arr.sort()
    i=0
    min_diff=1000
    while(i+n-1<m):
        diff=arr[i+n-1]-arr[i]
        if diff<min_diff:
            min_diff=diff
        i=i+1
    return min_diff
if __name__ == '__main__':
    arr=[3, 4, 1, 9, 56, 7, 9, 12]
    m=findmin(arr,5,len(arr))
    print(m)
