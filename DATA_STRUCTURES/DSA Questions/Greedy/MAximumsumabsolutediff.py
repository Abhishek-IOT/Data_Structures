def diff(arr):
    m=[0]*len(arr)
    for i in range(len(arr)-1):
        m[i]=abs(arr[i+1]-arr[i])
        print(m[i])
    return sum(m)+abs(arr[-1]-arr[0])


def maxAbs(arr,n):
    arr.sort()
    i=0
    j=n-1
    l=[]
    while(i<j):
        l.append(arr[i])
        l.append(arr[j])
        i+=1
        j-=1
    print(l)
    s=diff(l)
    print(s)


if __name__ == '__main__':
    arr=[1,2,4]
    maxAbs(arr,len(arr))