class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=[]
    def addEdge(self,u,v,w):
        self.graph.append([u,v,w])
    def printGraphwithwieght(self):
        self.graph=sorted(self.graph,key=lambda item:item[2])
        for source,destination,weight in self.graph:
            print(source,"=>",destination," with weights=",weight)
    def findparents(self,parent,i):
        if parent[i]==i:
            return i
        return self.findparents(parent,parent[i])
    def union(self,parent,rank,x,y):
        xroot=self.findparents(parent,x)
        yroot=self.findparents(parent,y)
        if rank[xroot]<rank[yroot]:
            parent[xroot]=yroot
        elif rank[xroot]>rank[yroot]:
            parent[yroot]=xroot
        else:
            parent[yroot]=xroot
            rank[xroot]+=1

    def krushkalalgorithm(self):
        result=[]
        i=0
        e=0
        self.graph = sorted(self.graph, key=lambda item: item[2])
        parent=[]
        rank=[]
        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)
        while e<self.vertices-1:
            u,v,w=self.graph[i]
            i=i+1
            x=self.findparents(parent,u)
            y=self.findparents(parent,v)
            if x!=y:
                e=e+1
                result.append([u,v,w])
                self.union(parent,rank,x,y)
        mincost=0
        for u,v,weight, in result:
            mincost+=weight
            print("%d -- %d == %d "%(u,v,weight))
        print("Minimum Spanning Tree=",mincost)

if __name__ == '__main__':
    g = Graph(4)
    g.addEdge(0, 1, 10)
    g.addEdge(0, 2, 6)
    g.addEdge(0, 3, 5)
    g.addEdge(1, 3, 15)
    g.addEdge(2, 3, 4)
    g.printGraphwithwieght()
    g.krushkalalgorithm()