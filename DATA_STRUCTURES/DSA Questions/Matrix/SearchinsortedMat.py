"""
Search a Element in a row wise and column wise sorted matrix
We will implement the binary search technique to see that the element is there and cut the next half of element by chrcking the values.
"""


def PrintMat(mat,row,col):
    for i in range(row):
        print("[",end="")
        for j in range(col):
            print(mat[i][j],end=",")
        print("]")
def SearchinMat(mat,row,col,element):
    i=0
    j=col-1
    while(i>=0 and j>=0 and i<row and j<col):
        if mat[i][j]==element:
            return i,j
        elif mat[i][j]>element:
            j=j-1
        else:
            i=i+1
    return -1
if __name__ == '__main__':
    mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    PrintMat(mat,3,4)
    m=SearchinMat(mat,3,4,11)
    if m==-1:
        print("Not Found")
    else:
        print("Found at the index",m[0],m[1])
