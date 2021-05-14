def chocolatedistrubtion(arr,n,m):
    if m==0 or n==0:
        return 0
    if n<m:
        return -1
    arr.sort()
    min_val=arr[0]
    max_val=arr[n-1]
    mind=max_val-min_val
    for i in range(n-m+1):
        mind=min(mind,arr[i+m-1]-arr[i])
        print(mind)
    return mind

if __name__ == '__main__':
    arr=[3, 4, 1, 9, 56, 7, 9, 12]
    m=5
    n=len(arr)
    yoyo=chocolatedistrubtion(arr,n,m)
    print(yoyo)
