def shortestjobnonprempt(mat):
    compl=[mat[0][0]]
    for i in range(len(mat)):
        compl.append(compl[i]+mat[i][1])
    for i in range(1,len(compl)):
        print(compl[i-1],"to",compl[i],"==>",mat[i-1][2])
    compl.pop(0)
    print(compl)
    turnaround=[0]*len(compl)
    for i in range(len(compl)):
        turnaround[i]=compl[i]-mat[i][0]
    print(turnaround)
    print("Average Turn Around Time =",sum(turnaround)/len(turnaround))
    watingtime=[0]*len(compl)
    for i in range(len(turnaround)):
        watingtime[i]=turnaround[i]-mat[i][1]
    print(watingtime)
    print("Average Waiting Time=",sum(watingtime)/len(watingtime))


if __name__ == '__main__':
    mat=[[1,3,"P1"],[2,4,"P2"],[1,2,"P3"],[4,4,"P4"]]
    mat=sorted(mat,key=lambda x:x[1])
    shortestjobnonprempt(mat)