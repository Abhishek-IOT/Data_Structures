def reverse(arr,arr2):
    i=len(arr)
    while(i>0):
        arr2=arr2+arr[i-1]
        i=i-1
    return arr2

def palin(arr):
    print(arr)
    arr2=""
    arr2=reverse(arr,arr2)
    print(arr2)
    if arr2==arr:
        print("yes")
    else:
        print("no")
if __name__ == '__main__':
    s="abc"
    palin(s)

