"""
Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
INPUT=[-2, -3, 4, -1, -2, 1, 5, -3]
OUTPUT=7
Solved using dynamic programming
"""
def maxsubstring(arr,size):
    max_so_far=0
    max_ending=0
    for i in range(size):
        max_ending=max_ending+arr[i]
        if(max_so_far<max_ending):
            max_so_far=max_ending
        if max_ending<0:
            max_ending=0
    return max_so_far
if __name__ == '__main__':
    arr=[-2, -3, 4, -1, -2, 1, 5, -3]
    m=maxsubstring(arr,len(arr))
    print(m)
