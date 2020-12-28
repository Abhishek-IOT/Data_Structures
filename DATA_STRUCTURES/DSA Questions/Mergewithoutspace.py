"""

Given two sorted arrays arr1[] of size N and arr2[] of size M.
Each array is sorted in non-decreasing order.
Merge the two arrays into one sorted array in non-decreasing order
 without using any extra space.
 LOGIC=First use the last index of the 1st array and then compare it with the array2 (if arr1[i]>arr[j]
 Then swap the elements and then merge them.
"""
def sort(arr,n):
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    return arr
def merge(arr1,arr2,n1,n2):
    i=n1-1
    j=0
    while i!=0 and j<n2:
        # print(arr1[i],arr2[j])
        if(arr1[i]>arr2[j]):
            temp=arr1[i]
            arr1[i]=arr2[j]
            arr2[j]=temp
        i=i-1
        j=j+1
    for m in range(n1):
        print(arr1[m],end="\n")
    print("The next array")
    for m in range(n2):
        print(arr2[m],end="\n")
    Sort1=sort(arr1,n1)
    Sort2=sort(arr2,n2)
    for m in range(n1):
        print(Sort1[m],end=" ")
    for m in range(n2):
        print(Sort2[m],end=" ")
if __name__ == '__main__':
    arr1=[1, 3, 5, 7]
    arr2=[0, 2, 6, 8, 9]
    merge(arr1,arr2,len(arr1),len(arr2))