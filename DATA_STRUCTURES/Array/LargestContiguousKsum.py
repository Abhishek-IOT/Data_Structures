def largestsumprint(arr,n,k):
    i=0
    j=k-1
    l=[]
    while(j-i+1==k and j!=len(arr)):
        s=0
        for o in range(i,j+1):
            s=s+arr[o]

        l.append(s)
        i=i+1
        j=j+1

    return l

if __name__ == '__main__':
    arr=[10,1,11,20,2,3]
    l=largestsumprint(arr,len(arr),3)
    for i in range(len(l)):
        print(l[i],end=" ")
    print()
    maxi=max(l)
    print("Maximum sum in arr of k subarray=",maxi)
