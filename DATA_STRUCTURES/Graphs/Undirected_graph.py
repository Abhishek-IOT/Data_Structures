class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.adj_list={}
        for node in self.vertices:
            self.adj_list[node]=[]

    def addedge(self,source,destination):
        self.adj_list[source].append(destination)
        self.adj_list[destination].append(source)

    def printGraph(self):
        for node in self.vertices:
            print(node,"=>",self.adj_list[node])
if __name__ == '__main__':
    all_edge=[('A','B'),('B','C'),('B','D'),('B','E')]
    vertices=['A','B','C','D','E']
    g=Graph(vertices)
    # g.printGraph()
    for source,destination in all_edge:
        g.addedge(source,destination)
    g.printGraph()

