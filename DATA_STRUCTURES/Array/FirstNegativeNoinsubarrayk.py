def FirstNegativeNo(arr,n,k):
    i=0
    j=k-1
    l=[]
    while(j-i+1==k and j!=len(arr)):
        flag=0
        for o in range(i,j+1):
            if arr[o]<0:
                l.append(arr[o])
                flag=1
                break
        if flag==0:
            l.append(0)
        i+=1
        j=j+1
    print(l)
if __name__ == '__main__':
    arr=[-8, 2, 3, -6, 10]
    n=len(arr)
    FirstNegativeNo(arr,n,k=2)
