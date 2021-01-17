def convert(s,d):
    t=0
    for i in range(len(s)):
        s=s+" "
        if s[i]=='I' and s[i+1]=='X':
            return 9
        if s[i]=='I' and s[i+1]=='V':
            return 4
        elif s[i] in d:
            t = t + d[s[i]]
    return t

if __name__ == '__main__':
    d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    s='DM'
    t=convert(s,d)
    print(t)
