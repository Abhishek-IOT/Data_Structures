def reverse(arr):
    l=len(arr)
    i=l
    while(i>0):
        print(arr[i-1],end=" ")
        i=i-1
    return arr


if __name__ == '__main__':
    arr=["h","e","l","l","o"]
    r=reverse(arr)
    print(r)
