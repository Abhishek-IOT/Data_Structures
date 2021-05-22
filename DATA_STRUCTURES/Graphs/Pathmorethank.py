class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=[[] for i in range(vertices)]
    def addEdge(self,u,v,w):
        self.graph[u].append([v,w])
        self.graph[v].append([u,w])
    def pathmorethank(self,source,k):
        path=[False]*(self.vertices)
        path[source]=1
        return self.pathmorethankutil(source,k,path)
    def pathmorethankutil(self,source,k,path):
        if k<=0:
            return True
        i=0
        while i!=len(self.graph[source]):
            v=self.graph[source][i][0]
            w=self.graph[source][i][1]
            i+=1
            if path[v]==True:
                continue
            if w>=k:
                return True
            path[v]=True
            if self.pathmorethankutil(v,k-w,path):
                return True
            path[v]=False
        return False

if __name__ == '__main__':
    g=Graph(9)
    g.addEdge(0, 1, 4)
    g.addEdge(0, 7, 8)
    g.addEdge(1, 2, 8)
    g.addEdge(1, 7, 11)
    g.addEdge(2, 3, 7)
    g.addEdge(2, 8, 2)
    g.addEdge(2, 5, 4)
    g.addEdge(3, 4, 9)
    g.addEdge(3, 5, 14)
    g.addEdge(4, 5, 10)
    g.addEdge(5, 6, 2)
    g.addEdge(6, 7, 1)
    g.addEdge(6, 8, 6)
    g.addEdge(7, 8, 7)
    src=0
    k=70
    if g.pathmorethank(src,k):
        print("Yes")
    else:
        print("Np")

