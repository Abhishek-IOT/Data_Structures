def maxrow(arr,row,col):
    s = []
    for i in range(row):
        print(arr[i])
        count=0

        for j in range(col):
            if arr[i][j]==1:
                count=count+1
        print(count)
        s.append(count)
    print(s)
    store=0
    for i in range(len(s)):
        if s[i]==max(s):
            store=i
        else:
            pass
    print("row",store,"Contains",max(s),"of one's")
if __name__ == '__main__':
    arr=[[0, 1, 1, 1],
           [0, 0, 1, 1],
           [1, 1, 1, 1],
           [0, 0, 0, 0]]
    print(arr)
    maxrow(arr,4,4)
