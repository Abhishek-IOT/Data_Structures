def replace(s1,s2):
    s3=""
    for i in range(len(s1)):
        if s1[i]==s2[i]:
            s3=s3+s1[i]
        else:
            s3=s3+s2[i]
    return s3
def insert(s1,s2):
    s3=""
    if s1[-1]==s2[-1]:
        for i in range(len(s1)):
            if s1[i]==s2[i]:
                s3=s3+s1[i]
            else:
                s3=s3+s2[i]
        s3=s3+s2[-1]
    return s3
def edit(s1,s2):
    l1=len(s1)
    l2=len(s2)
    count=0
    if l1==l2:
        if s1==s2:
            return 0
        else:
            s3=replace(s1,s2)
            print(s3,"The same thing")
            count=count+1
    else:
        s3=insert(s1,s2)
        print(s3)
        count=count+1
    return count
if __name__ == '__main__':
    s1="gesek"
    s2="geek"
    c=edit(s1,s2)
    print("the no of count used",c)

