"""
Rotate a matrix by 90 degree in clockwise direction without using any extra space
Difficulty Level : Medium
 Last Updated : 10 Nov, 2020
Given a square matrix, turn it by 90 degrees in clockwise direction without using any extra space.

Examples:

Input:
1 2 3
4 5 6
7 8 9
Output:
7 4 1
8 5 2
9 6 3
Logic=First transpose the matrix and then reverse the rows of the matrix
"""

def transpose(a, b, row, col):
    for i in range(col):
        for j in range(row):
            b[i][j] = a[j][i]
    return b


def reverse(arr, row, col):
    temp = 0
    for i in range(row):
        start = 0
        end = col - 1
        while start < end:
            # temp = mat[i][start]

            # mat[i][start] = mat[i][end]
            # mat[i][start] = temp
            arr[i][start], arr[i][end] = arr[i][end], arr[i][start]
            start += 1
            end -= 1
    return arr


def do(mat, row, col):
    B = [[0 for x in range(row)] for y in range(col)]
    arr = transpose(mat, B, row, col)
    # print(arr,"arr at the do")
    reverse(arr, row, col)
    print(arr)


if __name__ == '__main__':
    row = 4
    col = 4
    A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9, 10, 11, 12],
     [13, 14, 15, 16]]

    # reverse(A,4,4)
    do(A,4,4)