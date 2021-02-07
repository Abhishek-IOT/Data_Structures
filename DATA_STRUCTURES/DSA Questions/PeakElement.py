"""
Peak Element is the element which is having more value than it's neighbor and if at index 0 and size-1 then check only one neighbor else both
"""
def PeakElement(arr):
    low=0
    high=len(arr)-1
    while(low<high):
        mid=low+(high-low)//2
        if mid>0 and mid<high-1:
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return arr[mid]
            if arr[mid-1]>arr[mid]:
                high=mid-1
            else:
                low=mid+1
        elif mid==0:
            if arr[0]>arr[1]:
                return arr[0]
            else:
                return arr[1]
        elif mid==high-1:
            if arr[high-1]>arr[high-2]:
                return arr[high-1]
            else:
                return arr[high-2]

if __name__ == '__main__':
    arr=[5,10,0,15]
    m=PeakElement(arr)
    print("The Peak Element is ",m)
