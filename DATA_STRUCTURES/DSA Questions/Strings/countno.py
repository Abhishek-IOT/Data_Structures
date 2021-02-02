def search(ii, needle, row, col, hay,
                    row_max, col_max):
    found=0
    if(row>=0 and col>=0 and col<col_max and row<row_max and needle[ii]==hay[row][col]):
        temp=hay[row][col]
        ii+=1
        hay[row][col]=0
        if (ii==len(needle)):
            found=1
        else:
            found+=search(ii,needle,row+1,col,hay,row_max,col_max)
            found+=search(ii,needle,row-1,col,hay,row_max,col_max)
            found+=search(ii,needle,row,col-1,hay,row_max,col_max)
            found+=search(ii,needle,row,col+1,hay,row_max,col_max)
        hay[row][col]=temp
    return found
if __name__ == '__main__':
    needle = "MAGIC"
    inputt = [
            ['D','D','D','G','D','D'],
            ['B','B','D','E','B','S'],
            ['B','S','K','E','B','K'],
            ['D','D','D','D','D','E'],
            ['D','D','D','D','D','E'],
            ['D','D','D','D','D','G']
           ]
    print(inputt)
    ans=0
    size=5
    for i in range(6):
        for j in range(6):
            ans+=search(0,needle,i,j,)