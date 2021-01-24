def binarysearch(arr,start,end,x):
    if end>=start:
        mid=start+(end-start)//2
        if arr[mid]==x:
            return mid
        elif arr[mid]>x:
            return binarysearch(arr,start,mid-1,x)
        elif arr[mid]<x:
            return binarysearch(arr,mid+1,end,x)
    else:
        return -1
def bishu(arr,power):
    index=binarysearch(arr,0,len(arr),power)
    s=0
    for i in range(index):
        s=s+arr[i]
    return s,index+1
if __name__ == '__main__':
    arr=[1,2,3]
    m=3
    yo=bishu(arr,m)
    print(yo[0],"The sum")
    print(yo[1],"Count of the soldiers")

