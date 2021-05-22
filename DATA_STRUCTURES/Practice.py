def kadane(arr):
    max_so=0
    max_end=0
    for i in range(len(arr)):
        max_end=max_end+arr[i]
        if max_so<max_end:
            max_so=max_end
        if max_end<0:
            max_end=0
    return max_so
if __name__ == '__main__':
    arr=[-1,-2,3,4,5]
    m=kadane(arr)
    print(m)