def value(arr):
    for i in range(len(arr)):
        if arr[i]==i+1:
            print("Yes")
            print("arr[",i+1,"]=",arr[i])
if __name__ == '__main__':
    arr=[1]
    value(arr)