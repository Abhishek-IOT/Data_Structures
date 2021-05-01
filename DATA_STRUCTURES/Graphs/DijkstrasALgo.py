import sys
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[[0 for i in range(vertices)]for j in range(vertices)]
    def printSol(self,dist):
        for node in range(self.V):
            print(node,"    ",dist[node])
    def minimumdistance(self,dist,splset):
        min=sys.maxsize
        for v in range(self.V):
            if dist[v]<min and splset[v]==False:
                min=dist[v]
                min_index=v
        return min_index
    def dijkstras(self,source):
        dist=[sys.maxsize]*self.V
        dist[source]=0
        splset=[False]*self.V
        for i in range(self.V):
            u=self.minimumdistance(dist,splset)
            splset[u]=True
            for v in range(self.V):
                if self.graph[u][v]>0 and splset[v]==False and dist[v]>dist[u]+self.graph[u][v]:
                    dist[v]=dist[u]+self.graph[u][v]
        self.printSol(dist)
if __name__ == '__main__':

    g=Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]
    g.dijkstras(0)
