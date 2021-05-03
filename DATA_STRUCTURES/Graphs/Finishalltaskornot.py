"""
In this we need to find a cycle and if cycle exists it means that job is not possible and vice versa.
"""
from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
    def iscyclicutil(self,v,visited,recstack):
        visited[v]=True
        recstack[v]=True
        for neighbor in self.graph[v]:
            if visited[neighbor]==False:
                if self.iscyclicutil(neighbor,visited,recstack)==True:
                    return True
            elif recstack[neighbor]==True:
                return True
        recstack[v]=False
        return False

    def iscyclic(self):
        visited=[False]*(self.vertices)
        recstack=[False]*(self.vertices)
        for i in range(self.vertices):
            if visited[i]==False:
                if self.iscyclicutil(i,visited,recstack)==True:
                    return True
        return False

    def printGraph(self):
        for node in range(self.vertices):
            print(node,"=>",self.graph[node])
if __name__ == '__main__':
    g=Graph(2)
    g.addEdge(1,0)
    # g.addEdge(0,1)
    g.printGraph()
    if g.iscyclic()==True:
        print("Job is not possible")
    else:
        print("Job is possible")