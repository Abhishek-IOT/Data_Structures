from queue import Queue
class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.adj_list={}
        for node in self.vertices:
            self.adj_list[node]=[]
    def addedge(self,source,destination):
        self.adj_list[source].append(destination)
        self.adj_list[destination].append(source)

    def bfstraversal(self):
        visited={}
        level={}
        parent={}
        bfstrav=[]
        queue=Queue()
        for node in self.adj_list.keys():
            visited[node]=False
            level[node]=-1
            parent[node]=None
        source="A"
        visited[source]=True
        level[source]=0
        queue.put(source)
        while not queue.empty():
            u=queue.get()
            bfstrav.append(u)
            for v in self.adj_list[u]:
                if not visited[v]:
                    visited[v]=True
                    parent[v]=u
                    level[v]=level[u]+1
                    queue.put(v)
        return bfstrav

if __name__ == '__main__':
    all_edge = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('B', 'E')]
    vertices = ['A', 'B', 'C', 'D', 'E']
    g = Graph(vertices)
    # g.printGraph()
    for source, destination in all_edge:
        g.addedge(source, destination)
    m=g.bfstraversal()
    print(*m)
    print(g.adj_list)