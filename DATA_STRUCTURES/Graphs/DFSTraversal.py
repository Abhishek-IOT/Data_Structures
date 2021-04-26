from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def dfsutil(self,v,visited):
        visited.add(v)
        print(v)
        for node in self.graph[v]:
            if node not in visited:
                self.dfsutil(node,visited)
    def dfs(self,v):
        visited=set()
        self.dfsutil(v,visited)

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is DFS from (starting from vertex 2)")
g.dfs(2)