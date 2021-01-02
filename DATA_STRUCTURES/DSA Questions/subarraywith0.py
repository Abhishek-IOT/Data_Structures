def sum(arr, size):
    s=set()
    sumi = 0
    for i in range(size):
        if arr[i] == 0:
            sumi = 0
            break
        else:
            sumi=sumi+arr[i]
            if sumi==0 or sumi in s:
                return True
            s.add(sumi)
    return False


if __name__ == '__main__':
    arr = [4, 2, -3, 1, 6]
    i = sum(arr, len(arr))
    print(i)
    if i == True:
        print("Yes")
    else:
        print("No")

