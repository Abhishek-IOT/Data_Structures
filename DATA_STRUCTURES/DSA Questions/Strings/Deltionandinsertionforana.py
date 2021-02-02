"""
No of Deletions and Insertion to make both the strings as anagram
I/P=s1='abc'
s2='cde'
we have to Map the s1 with frequency and then we can check that the string is present in
s2 if yes then we will decrease else we will increase the count and at last sum the count.

"""
def anagram(s1,s2):
    d={}
    for i in range(len(s1)):
        if s1[i] not in d:
            d[s1[i]]=1
        else:
            d[s1[i]]+=1
    for j in range(len(s2)):
        if s2[j] in d:
            d[s2[j]]-=1
        else:
            d[s2[j]]=1
    s=0
    print(d)
    for i in d.values():
        if i<0:
            i=(-1)*i
        s=s+i

    return s
if __name__ == '__main__':
    a='caty'
    b='actyyyy'
    m=anagram(a,b)
    print(m)