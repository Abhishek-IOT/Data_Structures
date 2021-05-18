class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.graph=[[0 for i in range(self.vertices)]for j in range(self.vertices)]
    def isbipartite(self,source):
        color=[-1]*self.vertices
        color[source]=1
        queue=[]
        queue.append(source)
        while queue:
            u=queue.pop()
            if self.graph[u][u]==1:
                return False
            for v in range(self.vertices):
                if self.graph[u][v]==1 and color[v]==-1:
                    color[v]=1-color[u]
                    queue.append(v)
                    print(color,"Iam",u,v)
                elif self.graph[u][v]==1 and color[v]==color[u]:
                    return False

        return True
if __name__ == '__main__':
    g = Graph(4)
    g.graph = [[0, 1, 0, 1],
               [1, 0, 1, 0],
               [0, 1, 0, 1],
               [1, 0, 1, 0]
               ]
    if g.isbipartite(0):
        print("YEs")
    else:
        print('No')
