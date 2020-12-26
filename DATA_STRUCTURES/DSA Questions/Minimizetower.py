"""
Minimize the heights
Given an array arr[] denoting heights of N towers and a positive integer K,
you have to modify the height of each tower either by increasing or decreasing them by K only once.
After modifying, height should be a non-negative integer. Find out what could be the possible minimum
difference of the height of shortest and longest towers after you have modified each tower.
Example1:
Input:
K = 2, N = 4
Arr[] = {1, 5, 8, 10}
Output: 5
Explanation: The array can be modified as
{3, 3, 6, 8}. The difference between
the largest and the smallest is 8-3 = 5.
"""
def minimize(arr,size,k):
    for i in range(size):
        if arr[i]<=k:
            arr[i]=arr[i]+k
        else:
            arr[i]=arr[i]-k
    print(arr)
    m=min(arr)
    m1=max(arr)
    diff=m1-m
    return diff
if __name__ == '__main__':
    arr=[3, 9, 12, 16, 20]
    m=minimize(arr,len(arr),3)
    print(m)
