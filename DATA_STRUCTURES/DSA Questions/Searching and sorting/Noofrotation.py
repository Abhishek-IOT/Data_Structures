"""
CountRotations or Index of Minimum Element in the sorted rotated array.
We have to find how many times the array is rotated we will do it with the help of binary search
"""
def countrotations(arr,low,high):
    if high<low:
        return 0
    if high==low:
        return low
    mid=low+(high-low)/2
    mid=int(mid)
    if mid<high and arr[mid+1]<arr[mid]:
        return mid+1
    if mid>low and arr[mid]<arr[mid-1]:
        return mid
    if arr[high]>arr[mid]:
        return countrotations(arr,low,mid-1)
    return countrotations(arr,mid+1,high)
if __name__ == '__main__':
    arr=[4,5,6,7,8,1,2,3]
    m=countrotations(arr,0,len(arr)-1)
    print(m)