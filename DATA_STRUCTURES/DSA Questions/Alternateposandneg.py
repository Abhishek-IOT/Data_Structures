"""
Rearrange array in alternating positive & negative items with O(1) extra space.
Given an array of positive and negative numbers, arrange them in an alternate fashion
 such that every positive number is followed by negative and vice-versa.
Order of elements in output doesn’t matter. Extra positive or negative elements should be moved to end.
HINT=Use Quick sort to sort the array so that O(1) can be used (We are not using the Merge sort because it will take O(n)Space.
Then we will have a sorted array and then we will just swap the elements till the negative index= postive index
Input:  arr[] = {1, 2, 3, -4, -1, 4}
Output: arr[] = {-4, 1, -1, 2, 3, 4}
"""


def quicksort(arr,low,high):
    if low<high:
        pi=part(arr,low,high)
        print(pi)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
    return arr
def part(arr,low,high):
    i=low-1
    pivot=arr[high-1]
    for j in range(low,high):
        if arr[j]<pivot:
            i=i+1
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
    t=arr[i+1]
    arr[i+1]=arr[high-1]
    arr[high-1]=t
    return i+1
def rearrange(arr):
    quicksort(arr,0,len(arr)-1)
    print(arr)
    negative_index=0
    print(arr[negative_index],"nega")
    for j in range(len(arr)):
        if arr[j]>0:
            postive_index=j
            break
    print(postive_index)
    while(negative_index!=postive_index):
        temp=arr[negative_index]
        arr[negative_index]=arr[postive_index]
        arr[postive_index]=temp
        negative_index=negative_index+2
        postive_index=postive_index+1
    print(arr)
if __name__ == '__main__':
    arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
    n = len(arr)
    rearrange(arr)