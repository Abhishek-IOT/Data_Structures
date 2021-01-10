"""
Sorted matrix
Basic Accuracy: 52.25% Submissions: 11716 Points: 1
Given an n x n matrix, where every row and column is sorted in non-decreasing order. Print all elements of matrix in sorted order.

Input:
The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer n denoting the size of the matrix.
 Then the next line contains the n x n elements in row wise order.
 Logic=First convert the matrix to a normal list and then sort and return that list
"""

def sort(arr,size):
    temp=0
    for i in range(size):
        for j in range(i,size):
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print(arr)
def convert(mat,row,col):
    arr=[]
    for i in range(row):
        for j in range(col):
            arr.append(mat[i][j])
    sort(arr,(row*col)-1)
    return arr
if __name__ == '__main__':
    mat=[[10, 20, 30, 40],
     [15, 25, 35, 45],
     [27, 29, 37, 48],
     [32, 33, 39, 50],
     ]
    con=convert(mat,4,4)
    print(con)
    # arr=[1,40,2,3,50]
    # sort(arr,5)