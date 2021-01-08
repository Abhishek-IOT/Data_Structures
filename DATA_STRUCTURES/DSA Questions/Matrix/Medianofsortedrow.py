"""
Given a row wise sorted matrix of
 size RxC where R and C are always odd, find the median of the matrix
 Input:
R = 3, C = 3
M = [[1, 3, 5],
     [2, 6, 9],
     [3, 6, 9]]

Output: 5

Explanation:
Sorting matrix elements gives us
{1,2,3,3,5,6,6,9,9}. Hence, 5 is median.
Logic=Transform the matrix in array and sort it then take the median
"""


def median(arr,row,col):
    arr1=[]
    for i in range(row):
        for j in range(col):
            arr1.append(arr[i][j])
    arr1.sort()
    print(arr1)
    med=len(arr1)/2
    print(med)
    print(arr1[round(med)])
if __name__ == '__main__':
    R = 3
    C = 1
    M = [[1], [2], [3]]
    median(M,R,C)