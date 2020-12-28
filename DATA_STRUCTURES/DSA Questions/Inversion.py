def inv(arr,n):
    c=0
    for i in range(n):
        for j in range(n):
            if(arr[i]>arr[j] and i<j):
                c=c+1
    return c
if __name__ == '__main__':
    arr=[8, 4, 2, 1]
    i=inv(arr,len(arr))
    print(i)


