import math
def mad(arr):
    s=0
    m=0
    for i in range( 0, len(arr)-1):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i]==arr[j] and arr[i]==arr[k]:
                    s=0
                s=s+abs(arr[i]-arr[j])+abs(arr[i]-arr[k])+abs(arr[j]-arr[k])
                m=max(m,s)
    return m


if __name__ == '__main__':

    try:
        test=int(input())
        for i in range(test):
            n=int(input())
            arr=[0 for i in range(n)]
            arr=list(map(int,input().split()))
            m=mad(arr)
            print(m)
    except:
        pass
