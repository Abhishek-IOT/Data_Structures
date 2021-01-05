"""
Chocolate Distribution Problem
Given an array A of positive integers of size N, where each value represents number of chocolates in a packet. Each packet can have variable number of chocolates. There are M students, the task is to distribute chocolate packets such that :
1. Each student gets one packet.
2. The difference between the number of chocolates given to the students having packet with maximum chocolates and student having packet with minimum chocolates is minimum
LOGIC=First sort the array and then traverse the array from ith index to no of students and then find the
minimum difference and then increment the i and no of students +1 so that we can traverse till last.
Input : arr[] = {3, 4, 1, 9, 56, 7, 9, 12} , m = 5
Output: Minimum Difference is 6
Explanation:
The set goes like 3,4,7,9,9 and the output
is 9-3 = 6
"""


def findmin(arr,n,m):
    if m==0 and n==0:
        return 0
    if n>m:
        return -1
    arr.sort()
    i=0
    min_diff=1000
    while(i+n-1<m):
        diff=arr[i+n-1]-arr[i]
        if diff<min_diff:
            min_diff=diff
        i=i+1
    return min_diff
if __name__ == '__main__':
    arr=[3, 4, 1, 9, 56, 7, 9, 12]
    m=findmin(arr,5,len(arr))
    print(m)
