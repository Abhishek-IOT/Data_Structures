from sys import maxsize
def yoyo(arr,n,k):
    for i in range(1,k+1):
        min=maxsize
        ind=-1
        for j in range(n):
            if arr[j]<min:
                min=arr[j]
                print(min,"I am the min babay")
                ind=j
        print(min)
        if min==0:
            break
        arr[ind]=-arr[ind]
        print(arr)
    print(sum(arr))
if __name__=='__main__':
    arr = [1, -2, -3, 4, 5]
    k = 3
    n = len(arr)
    yoyo(arr,n,k)