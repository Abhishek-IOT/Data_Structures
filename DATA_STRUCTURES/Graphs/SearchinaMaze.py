MAX=5
def issafe(row,col,mat,n,visited):
    if row==-1  or row==n or col==-1 or col==n or visited[row][col] or mat[row][col]==0:
        return False
    return True
def printPathutil(row,col,mat,n,path,possiblepath,visited):
    if row ==-1 or row==n or col==-1 or col==n or visited[row][col] or mat[row][col]==0:
        return
    if row ==n-1 and col==n-1:
        possiblepath.append(path)
        return
    visited[row][col]=True
    #checking downward
    if(issafe(row+1,col,mat,n,visited)):
        path+='D'
        printPathutil(row+1,col,mat,n,path,possiblepath,visited)
        path=path[:-1]
    #checking upward
    if(issafe(row-1,col,mat,n,visited)):
        path+="U"
        printPathutil(row-1,col,mat,n,path,possiblepath,visited)
        path=path[:-1]

    #checking Right
    if(issafe(row,col+1,mat,n,visited)):
        path+="R"
        printPathutil(row,col+1,mat,n,path,possiblepath,visited)
        path=path[:-1]

    #checking Left
    if(issafe(row,col-1,mat,n,visited)):
        path+="L"
        printPathutil(row,col-1,mat,n,path,possiblepath,visited)
        path=path[:-1]

    visited[row][col]=False
def printPath(mat,n):
    possiblepath=[]
    path=""
    visited=[[False for _ in range(MAX)]for _ in range(n)]
    printPathutil(0,0,mat,n,path,possiblepath,visited)
    for i in range(len(possiblepath)):
        print(possiblepath[i],end=" ")
if __name__ == '__main__':
    m = [[1, 0, 0, 0, 0],
         [1, 1, 1, 1, 1],
         [1, 1, 1, 0, 1],
         [0, 0, 0, 0, 1],
         [0, 0, 0, 0, 1]]
    n = len(m)

    printPath(m, n)
