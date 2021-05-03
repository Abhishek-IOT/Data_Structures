from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def outdegree(self):
        for node in range(self.vertices+1):
            print(node,"=>",len(self.graph[node]))

if __name__ == '__main__':
    g=Graph(10)
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
    g.outdegree()