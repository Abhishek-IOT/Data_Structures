class Edge:
    def __init__(self):
        self.source=0
        self.destination=0
        self.weight=0
class Graph:
    def __init__(self):
        self.V=0
        self.E=0
        self.edge=0
def createGraph(V,E):
    graph=Graph()
    graph.V=V
    graph.E=E
    graph.edge=[Edge() for i in range(graph.E)]
    print(graph.edge)
    return graph
def hasnegativeCycle(graph,source):
    v=graph.V
    E=graph.E
    dist=[10000 for i in range(V)]
    dist[source]=0
    for i in range(1,V):
        for j in range(E):
            u=graph.edge[j].source
            v=graph.edge[j].destination
            weight=graph.edge[j].weight
            if dist[u]!=10000 and dist[u]+weight<dist[v]:
                dist[v]=dist[u]+weight
    for i in range(E):
        u=graph.edge[i].source
        v=graph.edge[i].destination
        weight=graph.edge[i].weight
        if dist[u]!=10000 and dist[u]+weight<dist[v]:
            return True
    return False

if __name__ == '__main__':
    # Let us create the graph given in above example
    V = 5;  # Number of vertices in graph
    E = 8;  # Number of edges in graph
    graph = createGraph(V, E);

    # add edge 0-1 (or A-B in above figure)
    graph.edge[0].src = 0;
    graph.edge[0].dest = 1;
    graph.edge[0].weight = -1;
    graph.edge[1].src = 0;
    graph.edge[1].dest = 2;
    graph.edge[1].weight = 4;

    # add edge 1-2 (or B-C in above figure)
    graph.edge[2].src = 1;
    graph.edge[2].dest = 2;
    graph.edge[2].weight = 3;

    # add edge 1-3 (or B-D in above figure)
    graph.edge[3].src = 1;
    graph.edge[3].dest = 3;
    graph.edge[3].weight = 2;

    # add edge 1-4 (or A-E in above figure)
    graph.edge[4].src = 1;
    graph.edge[4].dest = 4;
    graph.edge[4].weight = 2;

    # add edge 3-2 (or D-C in above figure)
    graph.edge[5].src = 3;
    graph.edge[5].dest = 2;
    graph.edge[5].weight = 5;

    # add edge 3-1 (or D-B in above figure)
    graph.edge[6].src = 3;
    graph.edge[6].dest = 1;
    graph.edge[6].weight = 1;

    # add edge 4-3 (or E-D in above figure)
    graph.edge[7].src = 4;
    graph.edge[7].dest = 3;
    graph.edge[7].weight = -3;

    if hasnegativeCycle(graph,0):
        print("Yes cycle found")
    else:
        print("No")