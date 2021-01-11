def convert(mat,row,col,k):
    arr=[]
    for i in range(row):
        for j in range(col):
            arr.append(mat[i][j])
    arr.sort()
    print(arr)
    print(arr[k])
if __name__ == '__main__':
    mat=[[16, 28, 60, 64],
                   [22, 41, 63, 91],
                   [27, 50, 87, 93],
                   [36, 78, 87, 94 ]]
    k=3
    convert(mat,4,4,k-1)

