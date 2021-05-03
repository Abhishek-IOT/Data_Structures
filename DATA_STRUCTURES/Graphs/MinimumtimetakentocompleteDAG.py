from collections import defaultdict
class Graph:
    def __init__(self,vertices,edges):
        self.vertices=vertices
        self.edges=edges
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def printGraph(self):
        for node in range(self.vertices):
            print(node,"=>",self.graph[node])
    def openorder(self,n,m):
        indegree=[0]*(self.vertices+1)
        for i in self.graph:
            for j in self.graph[i]:
                indegree[j]+=1
        print(indegree)
        job=[0]*(self.vertices+1)
        queue=[]
        for i in range(1,self.vertices+1):
            if indegree[i]==0:
                queue.append(i)
                job[i]=1
        while queue:
            cur=queue.pop(0)
            for adj in self.graph[cur]:
                indegree[adj]-=1
                if indegree[adj]==0:
                    job[adj]=1+job[cur]
                    queue.append(adj)
        for i in range(1,self.vertices+1):
            print(job[i],end=" ")
        print()


if __name__ == '__main__':
    n=10
    m=13
    g = Graph(n, m)
    # Given Directed Edges of graph
    g.addEdge(1, 3)
    g.addEdge(1, 4)
    g.addEdge(1, 5)
    g.addEdge(2, 3)
    g.addEdge(2, 8)
    g.addEdge(2, 9)
    g.addEdge(3, 6)
    g.addEdge(4, 6)
    g.addEdge(4, 8)
    g.addEdge(5, 8)
    g.addEdge(6, 7)
    g.addEdge(7, 8)
    g.addEdge(8, 10)
    g.printGraph()
    g.openorder(n,m)