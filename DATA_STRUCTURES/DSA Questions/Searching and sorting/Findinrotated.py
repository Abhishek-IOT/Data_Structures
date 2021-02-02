"""
Program to find the element in the rotated array.....We have to use binary search for it.
First we will count that how many times the array is rotated(by using the index of minimum element) and then we will use binary search in both the sub parts to
see the element
1)From =search(arr,low,index)
2)From =search(arr,index+1,high)
"""

def countrotation(arr,low,high):
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
        return countrotation(arr,low,mid-1)
    return countrotation(arr,mid+1,high)
def search(arr,low,high,n):
    while(low<=high):
        mid = low + (high - low) / 2
        mid=int(mid)
        if arr[mid]==n:
            return True
        if n>arr[mid]:
            return search(arr,mid+1,high,n)
        if n<arr[mid]:
            return search(arr,low,mid-1,n)
    return False
if __name__ == '__main__':
    arr=[4,5,6,7,8,9,1,2,3]
    n=3
    m=countrotation(arr,0,len(arr)-1)
    print(m)
    to=search(arr,0,m,n)
    o=search(arr,m+1,len(arr)-1,n)
    print(to)
    print(o)
    if to==True or o==True:
        print("Yes Found")
    else:
        print("No Found")