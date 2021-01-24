"""
Minimum Swaps to Sort
Medium Accuracy: 50.0% Submissions: 38124 Points: 4
Given an array of n distinct elements. Find the minimum number of swaps required to sort the array in strictly increasing order.
Logic=Use merge sort it will give time complexity of O(nlogn)
"""
def mergesort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid:]
        mergesort(left)
        mergesort(right)
        i=j=k=0
        while(i<len(left) and j <len(right)):
            if (left[i]<right[j]):
               arr[k]=left[i]
               i+=1
            else:
                arr[k]=right[j]
                j+=1
            k=k+1
        while(i<len(left)):
            arr[k]=left[i]
            i=i+1
            k+=1
        while(j<len(right)):
            arr[k]=right[j]
            j=j+1
            k=k+1
    return arr
if __name__ == '__main__':
    arr=[100,50,60,20,32,10,202]
    m=mergesort(arr)
    print(m)