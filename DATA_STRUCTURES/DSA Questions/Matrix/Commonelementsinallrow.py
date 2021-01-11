def common(mat,row,col):
    mp=dict()
    for j in range(col):
        mp[mat[0][j]]=1
    print(mp)
    for i in range(1,row):
        for j in range(col):
            if mat[i][j] in mp.keys() and mp[mat[i][j]]==i:
                mp[mat[i][j]]=i+1
                if i==row-1:
                    print(mat[i][j])
    print(mp)
if __name__ == '__main__':
    mat = [[1, 2, 1, 4, 8],
           [3, 7, 8, 5, 1],
           [8, 7, 7, 3, 1],
           [8, 1, 2, 7, 9]]
    row=4
    col=5
    common(mat,4,5)
