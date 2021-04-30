m=8
n=8
def floodfillutil(screen,x,y,prevC,newC):
    if x<0 or y<0 or x>=m or y>=n or screen[x][y]!=prevC or screen[x][y]==newC:
        return
    screen[x][y]=newC
    floodfillutil(screen,x+1,y,prevC,newC)
    floodfillutil(screen,x-1,y,prevC,newC)
    floodfillutil(screen,x,y+1,prevC,newC)
    floodfillutil(screen,x,y-1,prevC,newC)


def floodfill(screen,x,y,newC):
    prevC=screen[x][y]
    floodfillutil(screen,x,y,prevC,newC)
if __name__ == '__main__':
    screen = [[1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 0],
              [1, 0, 0, 1, 1, 0, 1, 1],
              [1, 2, 2, 2, 2, 0, 1, 0],
              [1, 1, 1, 2, 2, 0, 1, 0],
              [1, 1, 1, 2, 2, 2, 2, 0],
              [1, 1, 1, 1, 1, 2, 1, 1],
              [1, 1, 1, 1, 1, 2, 2, 1]]
    x=4
    y=4
    floodfill(screen,x,y,3)
    for i in range(m):
        for j in range(n):
            print(screen[i][j],end=' ')
        print()

