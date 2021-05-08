v=4
INF=99999
def floydwarshal(graph):
    dist=list(map(lambda i:list(map(lambda j:j,i)),graph))
    for k in range(v):
        for i in range(v):
            for j in range(v):
                dist[i][j]=min(dist[i][j],dist[i][k]+dist[k][j])
    for i in range(v):
        print("[",end=' ')
        for j in range(v):
            print(dist[i][j],end=' ')
        print("]")
if __name__ == '__main__':
    graph = [[0, 5, INF, 10],
             [INF, 0, 3, INF],
             [INF, INF, 0, 1],
             [INF, INF, INF, 0]
             ]
    floydwarshal(graph)