import sys
def distance():
    pass

if __name__ == '__main__':
    n=int(input())
    m=int(input())
    k=int(input())
    arr=[[]]
    for i in range(n):
        for j in range(m):
            arr[i][j]=input()
    mini=sys.maxsize
    for i in range(k):
        start=int(input())
        end=int(input())
        move=int(input())
        m=distance()
        mini=min(mini,m)
        