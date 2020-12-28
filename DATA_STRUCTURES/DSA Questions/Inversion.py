"""
Given an array of integers. Find the Inversion Count in the array.

Inversion Count: For an array, inversion count indicates how far (or close)
the array is from being sorted. If array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum.
Formally, two elements a[i] and a[j] form an inversion if a[i] > a[j] and i < j.
Input: N = 5, arr[] = {2, 4, 1, 3, 5}
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5
has three inversions (2, 1), (4, 1), (4, 3).
"""
def inv(arr,n):
    c=0
    for i in range(n):
        for j in range(n):
            if(arr[i]>arr[j] and i<j):
                c=c+1
    return c
if __name__ == '__main__':
    arr=[2, 3, 4, 5, 6]
    i=inv(arr,len(arr))
    print(i)


