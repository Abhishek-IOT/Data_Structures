from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def dfsutil(self,v,visited):
        visited[v]=True
        print(v,end=' ')
        for i in self.graph[v]:
            if visited[i]==False:
                self.dfsutil(i,visited)
    def reverseOrderStack(self,v,visited,stack):
        visited[v]=True
        for i in self.graph[v]:
            if visited[i]==False:
                self.reverseOrderStack(i,visited,stack)
        stack.append(v)
    def printConnectedComponents(self):
        stack=[]
        visited=[False]*self.vertices
        for i in range(self.vertices):
            if visited[i]==False:
                self.reverseOrderStack(i,visited,stack)
        gr=self.getTrans()
        visited=[False]*self.vertices
        while stack:
            i=stack.pop()
            if visited[i]==False:
                gr.dfsutil(i,visited)
                print()

    def getTrans(self):
        g=Graph(self.vertices)
        for i in self.graph:
            for j in self.graph[i]:
                g.addEdge(j,i)
        return g

if __name__ == '__main__':
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(0, 2)
    g.addEdge(2, 1)
    g.addEdge(0, 3)
    g.addEdge(3, 4)
    visited=[False]*5
    stack=[]
    g.printConnectedComponents()