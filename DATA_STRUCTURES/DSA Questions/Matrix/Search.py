"""
Given an n x n matrix and a number x,
find the position of x in the matrix if it is present in it.
Otherwise, print “Not Found”. In the given matrix, every row
 and column is sorted in increasing order.
 The designed algorithm should have linear time complexity.
 Logic do binary or linear search
"""

def search(arr,row,x):
    i=0
    j=row-1
    while(i<row and j>=0):
        if arr[i][j]==x:
            return 1
        if arr[i][j]>x:
            j=j-1
        else:
            i=i+1
    return 0
if __name__ == '__main__':
    mat = [[10, 20, 30, 40],
           [15, 25, 35, 45],
           [27, 29, 37, 48],
           [32, 33, 39, 50]]
    if (search(mat, 4, 29))==1:
        print("Yes")
    else:
        print("No")