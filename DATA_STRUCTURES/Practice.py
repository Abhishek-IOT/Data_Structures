def sumpair(arr,n,k):
    i=0
    j=n-1
    while(i<=j):
        if arr[i]+arr[j]==k:
            return True
        elif arr[i]+arr[j]<k:
            i=i+1
        else:
            j=j-1
    return False
if __name__ == '__main__':
    arr=[1,5,9,10]
    k=16
    if sumpair(arr,len(arr),k):
        print("YEs")
    else:
        print("No")