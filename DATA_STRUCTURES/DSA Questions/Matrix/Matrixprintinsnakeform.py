"""
Question was to print the matrix in snake form
I/P=[[1-> 2->  3],
               |
    [4 <-5  <-6],
    |
    [7-> 8->  9],
              |
    [11 <-12 <-13]]
O/P=[1, 2, 3, 6, 5, 4, 7, 8, 9, 13, 12, 11]
"""


def printsnake(mat,row,col):
    e=[]
    for i in range(row):
        print(i)
        if i%2==0:
            for j in range(col):
                e.append(mat[i][j])
        else:
            for j in range(col-1,-1,-1):
                e.append(mat[i][j])

    return e
if __name__ == '__main__':
    mat=[[1,2,3],[4,5,6],[7,8,9],[11,12,13]]
    row=4
    col=3
    m=printsnake(mat,row,col)
    print(m)