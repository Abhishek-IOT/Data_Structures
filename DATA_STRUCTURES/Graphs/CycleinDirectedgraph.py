ad_list={
    "A":['C','B'],
    "B":['D'],
    "C":[],
    "D":["A","E"],
    "E":[]
}
color={}
parent={}
for u in ad_list.keys():
    color[u]='W'
    parent[u]=None
print(color)
print(parent)
def dfs(u,color,parent):
    color[u]='G'
    for v in ad_list[u]:
        if color[v]=='W':
            cycle=dfs(v,color,parent)
            if cycle==True:
                return True
        elif color[v]=='G':
            return True
    color[u]='B'
    return False
if __name__ == '__main__':
    iscycle=False
    for u in ad_list.keys():
        if color[u]=='W':
            iscycle=dfs(u,color,parent)
            if iscycle==True:
                break
    print("cycle found=",iscycle)





