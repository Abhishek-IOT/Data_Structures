def allper(s):
    if len(s)==0:
        return []
    if len(s)==1:
        return [s]
    else:
        l=[]
        for i in range(len(s)):
            m=s[i]
            tor=s[:i]+s[i+1:]
            for p in allper(tor):
                l.append([m]+p)
            return l
data=list('abc')
for p in allper(data):
    print(p)