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