"""
Spiral Printing of Matrix
Print a given matrix in spiral form
Difficulty Level : Medium
 Last Updated : 01 Dec, 2020
Given a 2D array, print it in spiral form. See the following examples.

Examples:

Input:  1    2   3   4
        5    6   7   8
        9   10  11  12
        13  14  15  16
Output: 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
"""
def Traverse(arr,end_row,col_end):
    k=0
    l=0
    while(k<end_row and l<col_end):
        for i in  range(l,col_end):
            print(arr[k][i],end=" ")
        k=k+1
        for i in range(k,end_row):
            print(arr[i][col_end-1],end=" ")
        col_end=col_end-1
        if k<end_row:
            for i in range(col_end-1,(l-1),-1):
                print(arr[end_row-1][i],end=" ")
            end_row=end_row-1
        if l<col_end:
            for i in  range(end_row-1,(k-1),-1):
                print(arr[i][l],end=" ")
            l=l+1
if __name__ == '__main__':
    a = [[1, 2, 3, 4, 5, 6],
         [7, 8, 9, 10, 11, 12],
         [13, 14, 15, 16, 17, 18]]
    Traverse(a,3,6)