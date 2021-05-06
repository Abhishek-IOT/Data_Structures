def kadaneAlgo(arr):
    max_end_here=0
    max_so_far=0
    for i in range(len(arr)):
        max_end_here=max_end_here+arr[i]
        if max_end_here>max_so_far:
            max_so_far=max_end_here
        if max_end_here<0:
            max_end_here=0

    print(max_end_here)
    return max_so_far
if __name__=='__main__':
    arr=[-2,-3,4,-1,-2,1,5,-3]
    m=kadaneAlgo(arr)
    print(m)