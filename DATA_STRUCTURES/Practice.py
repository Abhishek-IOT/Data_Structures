from collections import deque
def shortest(start,target,dict):
    if start==target:
        return 0
    if target not in dict:
        return 0
    level=0
    wordlen=len(start)
    qu=deque()
    qu.append(start)
    while(len(qu)>0):
        level+=1
        size=len(qu)
        for i in range(size):
            word=[j for j in qu.popleft()]
            for pos in range(wordlen):
                org=word[pos]
                for c in range(ord('A'),ord('Z')+1):
                    word[pos]=chr(c)
                    print(word)
                    if ("".join(word)==target):
                        print(word,"56565656")
                        return level+1

                    if ("".join(word) not in D):
                        continue
                    del D["".join(word)]
                    qu.append("".join(word))
                word[pos] = org
    return 0
if __name__ == '__main__':
    D = {}
    D['ABCD']=1
    D['EBAD']=1
    D['EBCD']=1
    D['XYZA']=1
    start="ABCV"
    target="EBCD"
    lev=shortest(start,target,D)
    print(lev)