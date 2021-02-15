class Meeting:
    def __init__(self,start,end,pos):
        self.start=start
        self.end=end
        self.pos=pos
def maxMeeting(l):
    n=len(l)
    l.sort(key=lambda x:x.end)
    ans=[]
    ans.append(l[0].pos)
    time=l[0].end
    for i in range(1,len(l)):
        if l[i].start>time:
            ans.append(l[i].pos)
            time=l[i].end
    for i in ans:
        print(i+1,end="  ")
if __name__ == '__main__':

    start=[ 1, 3, 0, 5, 8, 5 ]
    finish=[ 2, 4, 6, 7, 9, 9 ]
    l=[]
    for i in range(len(start)):
       l.append(Meeting(start[i],finish[i],i))
    maxMeeting(l)