from collections import defaultdict
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=defaultdict(list)
    def addEdge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)
    def graphcolor(self):
        res=[-1]*self.vertices
        res[0]=0
        available=[False]*self.vertices
        for u in range(1,self.vertices):
            for i in self.graph[u]:
                if res[i]!=-1:
                    available[res[i]]=True
            cr=0
            while(cr<self.vertices):
                if available[cr]==False:
                    break
                cr+=1
            res[u]=cr
            for i in self.graph[u]:
                if res[i]!=-1:
                    available[res[i]]=False
        for i in range(self.vertices):
            print("Vertex ",i,"==> Color",res[i])


if __name__ == '__main__':
    g1=Graph(5)
    g1.addEdge(0,1)
    g1.addEdge(0,2)
    g1.addEdge(1,2)
    g1.addEdge(1,3)
    g1.addEdge(2,3)
    g1.addEdge(3,4)
    g1.graphcolor()
    g2=Graph(5)
