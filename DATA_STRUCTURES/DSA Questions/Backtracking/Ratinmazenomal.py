n=4
def issafe(maze,x,y):
    if x>=0 and y>=0 and x<n and y<n and maze[x][y]==1:
        return True
    return False
def solvemaze(maze):
    sol=[[0 for i in range(n)]for j in range(n)]
    if solvemazeutil(maze,0,0,sol)==False:
        print("No such Solution Exist")
        return False
    return True
def solvemazeutil(maze,x,y,sol):
    if x==n-1 and y==n-1 and maze[x][y]==1:
        sol[x][y]=1
        return True
    if issafe(maze,x,y)==True:
        if sol[x][y]==1:
            return False
        sol[x][y]=1
        if solvemazeutil(maze,x+1,y,sol)==True:
            return True
        if solvemazeutil(maze,x-1,y,sol)==True:
            return True
        if solvemazeutil(maze,x,y+1,sol)==True:
            return True
        if solvemazeutil(maze,x,y-1,sol)==True:
            return True
        sol[x][y]=0
        return False
if __name__ == '__main__':
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]]
    if solvemaze(maze):
        print("Yes rat can go to destination")
    else:
        print("No rat rat can no go to destination")