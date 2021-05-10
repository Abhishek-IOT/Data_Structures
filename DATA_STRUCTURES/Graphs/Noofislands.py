from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def findsubset(self,parent,i):
        if parent[i]==-1:
            return i
        if parent[i]!=-1:
            return self.findsubset(parent,parent[i])
    def union(self,parent,x,y):
        parent[x]=y
    def iscyclic(self):
        parent=[-1]*(self.vertices)
        for i in self.graph:
            for j in self.graph[i]:
                x=self.findsubset(parent,i)
                y=self.findsubset(parent,j)
                if x==y:
                    return True
                self.union(parent,x,y)
if __name__ == '__main__':
    g=Graph(3)
    g.addEdge(0, 1)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    if g.iscyclic():
        print("YEs")
    else:
        print("No")


