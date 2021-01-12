"""
A Program to check if strings are rotations of each other or not
Difficulty Level : Medium
 Last Updated : 06 Nov, 2020
Given a string s1 and a string s2, write a snippet to say whether s2 is a rotation of s1?
(eg given s1 = ABCD and s2 = CDAB, return true, given s1 = ABCD, and s2 = ACBD , return false)
Logic=First make the concatenation of s1 and s1(Make it as temp) and then check that s2 is there in temp or not
if yes then they are else no.
"""
def rotation(s1,s2):
    l1=len(s1)
    l2=len(s2)
    if l1!=l2:
        return 0
    temp=s1+s1
    print(temp)
    if temp.count(s2)>0:
        return 1
    else:
        return 0
if __name__ == '__main__':
    string1 = "AACD"
    string2 = "ACDA"
    if rotation(string1,string2)==1:
        print("yes they are rotation")
    else:
        print("Nooooooooo")