"""
Trapping Rain Water
Given n non-negative integers representing an elevation map where the width of each bar is 1,
 compute how much water it is able to trap after raining.
LOGIC=Traverse the array from start to end.
For every element, traverse the array from start to that index and find the maximum height (a) and traverse the array from the current index to end and find the maximum height (b).
The amount of water that will be stored in this column is min(a,b) – array[i], add this value to total amount of water stored
Print the total amount of water stored.
Input= {3, 0, 2, 0, 4}
Output=0 + 3 + 1 + 3 + 0 = 7
"""


def maxwater(arr,size):
    res = 0
    for i in range(1,size-1):

        left=arr[i]
        for j in range(i):
            print(left, arr[j], "The max in left", max(left, arr[j]))
            left=max(left,arr[j])

        right=arr[i]
        for j in range(i+1,size):
            print(right, arr[j], "The max in right", max(right, arr[j]))
            right=max(right,arr[j])

        res=res+(min(right,left)-arr[i])
        print(res,"the res yo")
    return res
if __name__ == '__main__':
    arr=[3, 0, 2, 0, 4]
    m=maxwater(arr,len(arr))
    print(m)
