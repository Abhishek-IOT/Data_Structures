def median(arr,row,col):
    arr1=[]
    for i in range(row):
        for j in range(col):
            arr1.append(arr[i][j])
    arr1.sort()
    print(arr1)
    med=len(arr1)/2
    print(med)
    print(arr1[round(med)])
if __name__ == '__main__':
    R = 3
    C = 1
    M = [[1], [2], [3]]
    median(M,R,C)