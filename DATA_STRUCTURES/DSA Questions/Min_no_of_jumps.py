"""
Minimum number of jumps
Given an array of integers where each element represents
the max number of steps that can be made forward from that element.
Write a function to return the minimum number of jumps to reach the
 end of the array (starting from the first element).
If an element is 0, then cannot move through that element.
INPUT=1 3 5 8 9 2 6 7 6 8 9
OUTPUT=3
"""


# def minise(arr,size):
#     i=0
#     if size==1:
#         m=1
#     temp=arr[0]
#     m=0
#     while(i<size):
#         temp=temp+arr[i]
#         m=m+1
#         i=i+temp
#         print(temp)
#     print(m)
# if __name__ == '__main__':
#     arr=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
#     minise(arr,len(arr))
#
# Python3 program to find Minimum
# number of jumps to reach end

# Returns minimum number of jumps
# to reach arr[h] from arr[l]
def minJumps(arr, l, h):
    # Base case: when source and
    # destination are same
    if (h == l):
        return 0

    # when nothing is reachable
    # from the given source
    if arr[l] == 0:
        return float('inf')

    # Traverse through all the points
    # reachable from arr[l]. Recursively
    # get the minimum number of jumps
    # needed to reach arr[h] from
    # these reachable points.
    min = float('inf')
    for i in range(l + 1, h + 1):
        print("i=",i)
        if i < l + arr[l] + 1:
            jumps = minJumps(arr, i, h)
            print("Jumps","Jumps=",jumps)
            print(i,h)
            print(min)
            if (jumps != float('inf') and
                    jumps + 1 < min):
                min = jumps + 1
                print(min,"Minvalue ")

    return min


# Driver program to test above function
arr = [1, 4, 3 ,2 ,6 ,7]
n = len(arr)
print('Minimum number of jumps to reach',
      'end is', minJumps(arr, 0, n - 1))

# This code is contributed by Soumen Ghosh
