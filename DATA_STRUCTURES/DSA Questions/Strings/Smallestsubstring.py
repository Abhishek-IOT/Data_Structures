no_char=256
def findsub(s,pat):
    l1=len(s)
    l2=len(pat)
    if l1<l2:
        print("NO such Pattern exist")
        return ""
    hash_pat=[0]*no_char
    hash_s=[0]*no_char
    for i in range(l2):
        hash_pat[ord(pat[i])]+=1
    start=0
    start_inx=-1
    min_len=float('inf')
    count=0
    for j in range(l1):
        hash_s[ord(s[j])]+=1
        if (hash_pat[ord(s[j])!=0] and hash_s[ord(s[j])]<=hash_pat[s[j]]):
            count+=1
        if count==l2:
            while(hash_s[ord(s[start])]>hash_pat[ord(s[start])] or
            hash_pat[ord(s[start])]==0):
                if hash_s[ord(s[start])]>hash_pat[ord(s[start])]:
                    hash_s[ord(s[start])]-=1
                start+=1
            len_wind=j-start+1
            print(len_wind)
            if min_len>len_wind:
                min_len=len_wind
                start_inx=start
    print(min_len)
    if start_inx==-1:
        print("NO such string possible")
        return ""
    return s[start:start_inx+min_len]


if __name__ == '__main__':
    s = "this is a test string"
    pat = "tist"
    findsub(s,pat)
