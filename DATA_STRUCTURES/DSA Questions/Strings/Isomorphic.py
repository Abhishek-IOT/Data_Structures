"""
Isomorphic Strings
Easy Accuracy: 47.07% Submissions: 13069 Points: 2
Given two strings 'str1' and 'str2', check if these two strings are isomorphic to each other.
Two strings str1 and str2 are called isomorphic if there is a one to one mapping possible for every character of str1 to every character of str2 while preserving the order.
Note: All occurrences of every character in ‘str1’ should map to the same character in ‘str2’
Logic make a dictionary or map of the characters and then make check the occurence of string 2 in string 1.If present then increase the index else pass.
"""
def iso(s1,s2):
    d={}
    l1=len(s1)
    l2=len(s2)
    if l1!=l2:
        return 0
    for i in range(l1):
        if s1[i] not in d:
            d[s1[i]]=s2[i]
    index=0
    for i in range(l1):

        if s2[i]==d[s1[i]]:
            index+=1
        else:
            pass
    if index==l1:
        print("Yes")
        return 1
    else:
        print("No")
        return 0
if __name__ == '__main__':
    s1="abcb"
    s2='xyzy'
    m=iso(s1,s2)
    if m==1:
        print("Yes")
    else:
        print("Np")