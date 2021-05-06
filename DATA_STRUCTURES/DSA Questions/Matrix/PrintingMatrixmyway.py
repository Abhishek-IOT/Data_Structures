def printMat(Mat,row,col):
    for i in range(col+1):
        print("  ",i,end=' | ')
    print()
    for i in range(row+1):
        print(i,end=' ')
        print("[",end='')
        for j in range(col+1):
            print(Mat[i][j],end='| ')
        print("]")
if __name__ == '__main__':
    dp=[[True False False False False False False False False False False False ]
[True False True False False False False False False False False False ]
[True False True True False True False False False False False False ]
[True False True True False True False True False True True False ]
[True False True True False True False True True True True True ]
[True False True True False True False True True True True True ]]