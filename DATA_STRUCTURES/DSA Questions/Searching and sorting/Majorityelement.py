"""
Made a map to check the count of characters and then checked the condition and returned the value.If we want to check the value in dictionary we will use
d.values() function.
"""
def majority(s,size):
    if size==0:
        return -1
    d={}
    for i in range(size):
        if s[i] not in d:
            d[s[i]]=1
        else:
            d[s[i]]+=1
    for i in d.values():
        if i>=size//2:
            return d[i]


if __name__ == '__main__':
    arr=[3,2,2,4]
    m=majority(arr,len(arr))
    print(m)
