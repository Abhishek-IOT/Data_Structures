"""
Row with max 1s
Medium Accuracy: 37.09% Submissions: 9529 Points: 4
Given a boolean 2D array of n x m dimensions where each row is sorted.
Find the 0-based index of the first row that has the maximum number of 1's.
Input:
N = 4 , M = 4
Arr[][] = {{0, 1, 1, 1},
           {0, 0, 1, 1},
           {1, 1, 1, 1},
           {0, 0, 0, 0}}
Output: 2
Explanation: Row 2 contains 4 1's (0-based
indexing).
"""
def maxrow(arr,row,col):
    s = []
    for i in range(row):
        print(arr[i])
        count=0

        for j in range(col):
            if arr[i][j]==1:
                count=count+1
        print(count)
        s.append(count)
    print(s)
    store=0
    for i in range(len(s)):
        if s[i]==max(s):
            store=i
        else:
            pass
    print("row",store,"Contains",max(s),"of one's")
if __name__ == '__main__':
    arr=[[0, 1, 1, 1],
           [0, 0, 1, 1],
           [1, 1, 1, 1],
           [0, 0, 0, 0]]
    print(arr)
    maxrow(arr,4,4)
