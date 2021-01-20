def countsq(arr,value):
    for i in range(len(arr)):
        if arr[i]==value:
            return
if __name__ == '__main__':
    arr=[1,4,9,16]
    ret=countsq(arr,9)
    print(ret)