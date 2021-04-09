max_no=256
def getcount(s):
    map=[0]*max_no
    for i in s:
        map[ord(i)]+=1
    return map
def nonrepeat(s):
    map=getcount(s)
    ind=-1
    k=0
    for i in s:
        if map[ord(i)]==1:
            ind=k
            break
        k+=1
    return ind
if __name__ == '__main__':
    s="geeksforgeeks"
    m=nonrepeat(s)
    print(s[m])

