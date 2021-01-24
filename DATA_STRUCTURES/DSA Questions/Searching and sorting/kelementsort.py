"""
K-th element of two sorted Arrays
Medium Accuracy: 16.57% Submissions: 851 Points: 4
Given two sorted arrays arr1 and arr2 of size M and N respectively and an element K. The task is to
find the element that would be at the k’th position of the final sorted array.
Logic=Merge the array with using merge sort technique and just return the k-1 element
"""
def merge(arr1,arr2):
    i=j=k=0
    length=len(arr1)+len(arr2)
    arr=[0]*length
    while i<len(arr1) and j<len(arr2):
        if arr1[i]<arr2[j]:
            arr[k]=arr1[i]
            i+=1
        else:
            arr[k]=arr2[j]
            j=j+1
        k+=1
    while i <len(arr1):
        arr[k]=arr1[i]
        i=i+1
        k=k+1
    while(j<len(arr2)):
        arr[k]=arr2[j]
        j=j+1
        k=k+1
    return arr

def kth(arr1,arr2,k):
    m=merge(arr1,arr2)
    print(m)
    return m[k-1]
if __name__ == '__main__':
    arr1=[2, 3, 6, 7, 9]
    arr2=[1, 4, 8, 10]
    k=5
    m=kth(arr1,arr2,k)
    print(m)
