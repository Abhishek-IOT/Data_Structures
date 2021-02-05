"""
Floor in a Sorted Array
Difficulty Level : Easy
 Last Updated : 25 May, 2020
Given a sorted array and a value x, the floor of x is the largest element in array smaller than or equal to x. Write efficient functions to find floor of x.

Examples:

Input : arr[] = {1, 2, 8, 10, 10, 12, 19}, x = 5
Output : 2
2 is the largest element in
arr[] smaller than 5.
Logic is that we will apply binary search so that we can cut half that is not required
and then we will check that mid-1th element is not less than x and x>arr[mid]
and if x>arr[mid] we will check in next half and if less then we will check in first half
"""
def floorSearch(arr,low,high,x):
    if low>high:
        return -1
    if x>arr[high]:
        return high

    mid=low+(high-low)//2
        # print(mid)
    if x==arr[mid]:
        # print("Mid")
        return mid
    if mid>0 and arr[mid-1]<=x and x<arr[mid]:
            # print("Mid-1")
        return mid-1
    if x>arr[mid]:
            # print("YOYO")
        return floorSearch(arr,mid+1,high,x)
    else:
        return floorSearch(arr,low,mid-1,x)
if __name__ == '__main__':
    arr=[1,2,3,4,10,20]
    x=21
    m=floorSearch(arr,0,len(arr)-1,x)
    print(arr[m])