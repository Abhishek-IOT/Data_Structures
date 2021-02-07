"""
Search an Element in Bitonic Array.Bitonic Array is first increasing and then decreasing.
So we will find the Peak ELement and then we will divide the array and have binary search for increasing and decreasing array.
"""
def PeakELement(arr):
    low=0
    high=len(arr)-1
    while(low<high):
        mid=low+(high-low)//2
        if mid>0 and mid<high-1:
            if arr[mid]>arr[mid+1] and arr[mid]>arr[mid-1]:
                return mid
            elif arr[mid-1]>arr[mid]:
                high=mid-1
            else:
                low=mid+1
        elif mid==0:
            if arr[0]>arr[1]:
                return 0
            else:
                return 1
        elif mid==high-1:
            if arr[high-1]>arr[high-2]:
                return high-1
            else:
                return high-2


def BinarSearch(arr,low,high,x):
    print(arr[low],arr[high])
    if arr[low]<arr[high]:
        while(low<=high):

            mid=low+(high-low)//2
            print(mid,"YO is is")
            if arr[mid]==x:
                return 1
            elif arr[mid]>x:
                high=mid-1
            elif arr[mid]<x:
                low=mid+1
    else:
        while (low <= high):
            mid = low + (high - low) // 2
            if arr[mid] == x:
                return 1
            elif arr[mid] > x:
                low=mid+1
            elif arr[mid] < x:
                high=mid-1
    return 0

if __name__ == '__main__':
    arr=[1,3,8,12,4,2]
    yo=PeakELement(arr)
    print(yo)
    # print(arr[:yo-1])
    # print(arr[yo:])
    x=1

    print(arr[yo:len(arr)])
    first=BinarSearch(arr,0,yo-1,x)
    second=BinarSearch(arr,yo,len(arr)-1,x)
    if first==1 or second==1:
        print("Yes Found")
    else:
        print("Not Found")