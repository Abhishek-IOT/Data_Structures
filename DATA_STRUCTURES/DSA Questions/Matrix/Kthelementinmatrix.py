"""
Kth element in Matrix
Medium Accuracy: 47.64% Submissions: 9554 Points: 4
Given a N x N matrix, where every row and column is sorted in non-decreasing order. Find the kth smallest element in the matrix.

Example 1:
Input:
N = 4
mat[][] =     {{16, 28, 60, 64},
                   {22, 41, 63, 91},
                   {27, 50, 87, 93},
                   {36, 78, 87, 94 }}
K = 3
Output: 27
Explanation: 27 is the 3rd smallest element.
Logic=First convert the matrix to array and then sort the array then print the kth element.
"""
def convert(mat,row,col,k):
    arr=[]
    for i in range(row):
        for j in range(col):
            arr.append(mat[i][j])
    arr.sort()
    print(arr)
    print(arr[k])
if __name__ == '__main__':
    mat=[[10, 20, 30, 40],
                   [15, 25, 35, 45],
                   [24, 29, 37, 48],
                   [32, 33, 39, 50]]
    k=7
    convert(mat,4,4,k-1)

