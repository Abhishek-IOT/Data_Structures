class Meeting:
    def __init__(self,start,end,pos):
        self.start=start
        self.end=end
        self.pos=pos
def Meet(l,n):
    ans=[]
    l.sort(key=lambda x:x.end)
    ans.append(l[0].pos)
    time=l[0].end
    for i in range(1,n):
        if l[i].start>time:
            ans.append(l[i].pos)
            time=l[i].end
    for i in ans:
        print(i+1,end=" ")


s = [1, 3, 0, 5, 8, 5]
f = [2, 4, 6, 7, 9, 9]
n=len(s)
l=[]
for i in range(n):
    l.append(Meeting(s[i],f[i],i))

Meet(l,n)

