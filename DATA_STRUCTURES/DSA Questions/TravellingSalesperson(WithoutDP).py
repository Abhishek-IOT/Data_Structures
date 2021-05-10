from sys import maxsize
from itertools import permutations
V=4
def TSP(graph,s):
    ver=[]
    for i in range(V):
        if i!=s:
            ver.append(i)
    minpath=maxsize
    nextpermutation=permutations(ver)
    for i in nextpermutation:
        cur=0
        k=s
        for j in i:
            cur+=graph[k][j]
            k=j
        cur+=graph[k][s]
        minpath=min(minpath,cur)
    return minpath
if __name__ == '__main__':
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],
             [15, 35, 0, 30], [20, 25, 30, 0]]
    s = 0
    m=TSP(graph,s)
    print(m)