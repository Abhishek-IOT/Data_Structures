"""
In this we have to go 8 directions that means diagonally also.
"""
class Graph:
    def __init__(self,row,col,g):
        self.row=row
        self.col=col
        self.graph=g
    def dfs(self,u,v,visited):
        if u<0 or v<0 or v>=self.row or u>=self.col:
            return
        if self.graph[u][v]==0:
            return
        if visited[u][v]==False:
            visited[u][v]=1
            self.dfs(u+1,v,visited)
            self.dfs(u-1,v,visited)
            self.dfs(u,v+1,visited)
            self.dfs(u,v-1,visited)
            self.dfs(u+1,v+1,visited)
            self.dfs(u-1,v-1,visited)
            self.dfs(u+1,v-1,visited)
            self.dfs(u-1,v+1,visited)


    def countislands(self):

        visited=[[False for i in range(self.col)]for j in range(self.row)]
        c=0
        for i in range(self.row):
            for j in range(self.col):
                visited[i][j]=0
        for i in range(self.row):
            for j in range(self.col):
                if visited[i][j]==False and self.graph[i][j]==1:
                    self.dfs(i,j,visited)
                    c=c+1
        return c
if __name__ == '__main__':
    graph = [[1, 1, 0, 0, 0],
             [0, 1, 0, 0, 1],
             [1, 0, 0, 1, 1],
             [0, 0, 0, 0, 0],
             [1, 0, 1, 0, 1]]
    row=len(graph)
    col=len(graph[0])
    g=Graph(row,col,graph)
    print(g.countislands())