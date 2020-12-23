"""
This is a question to sort an array of 0,1,2
Given an array of size N containing only 0s, 1s, and 2s; sort the array in ascending order.
Example=
Input=1, 0, 2, 1, 1
Output=0 1 1 1 2
"""
def sort(arr,arr_size):
    l=0
    mid=0
    high=arr_size-1
    while mid<=high:
        if arr[mid]==0:
            temp=arr[mid]
            arr[mid]=arr[l]
            arr[l]=temp
        elif arr[mid]==1:
            mid=mid+1

        else:
            temp=arr[mid]
            arr[mid]=arr[high]
            arr[high]=temp
            mid=mid+1
            high=high-1

    return arr
def display(arr):
    for i in arr:
        print(i,end=" ")
if __name__ == '__main__':
    arr=[1,0,2,1,1]
    print(arr,len(arr))
    s=sort(arr,len(arr))
    display(arr)


