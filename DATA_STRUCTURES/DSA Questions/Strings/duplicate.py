def duplicate(arr):
    mp=dict()
    test_list = list(map(chr, range(97, 123)))
    for i in range(len(test_list)):
        mp[test_list[i]]=1

    print(mp)
    for i in range(len(arr)):
        if arr[i] in mp.keys():
            mp[arr[i]]+=1
        else:
            continue
    for i in mp:
        if mp[i]>2:
            print(mp[i],i)
    print(mp)
if __name__ == '__main__':
    s="test string"
    duplicate(s)