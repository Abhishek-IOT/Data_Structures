def sumzero(arr):
    l=len(arr)
    for i in range(l):
        j=0
        sum=0
        count=0
        if arr[i]!=sum:
            sum=sum+arr[j]
            j=j+1
        else:
            count=count+1
    return count
if __name__ == '__main__':
    arr=[0,0,5,5,0,0]
    m=sumzero(arr)
    print(m)
