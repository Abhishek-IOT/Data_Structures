def sort(arr,n):
    for i in range(0, n):
        index = arr[i] % n
        # print(index)
        arr[index] += n
        # print(arr[index],"+++++++++++++++")
    # for i in range(n):
    #     print(arr[i],end=" ")
    for i in range(0, n):
        # print(arr[i],",,,",n)
        # print(arr[i]/n)
        if (arr[i] / n) >= 2:
            print(i, end=" ")
arr = [1, 2, 3, 1, 3, 6,6]
arr_size = len(arr)
sort(arr,arr_size)
# 1 8 14 7 7