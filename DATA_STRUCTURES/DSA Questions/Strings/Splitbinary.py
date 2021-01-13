"""
Split the binary string into substrings with equal number of 0s and 1s
Difficulty Level : Easy
 Last Updated : 20 Nov, 2019
Given a binary string str of length N, the task is to find the maximum count of substrings str can be divided into such that all the substrings are balanced \
i.e. they have equal number of 0s and 1s. If it is not possible to split str satisfying the conditions then print -1.
Input: str = “0100110101”
Output: 4
The required substrings are “01”, “0011”, “01” and “01”.
Logic=Make the count0 and check the count of 0 and count of 1(if count0==count1) Make then increment the count
and if the count0!=count1 then return -1.

"""
def splitting(s,size):
    c0=0
    c1=0
    count=0
    for i in range(size):
        if s[i]=='0':
            c0+=1
        if s[i]=='1':
            c1+=1
        if c1==c0:
            count=count+1
    if c0!=c1:
        return -1
    return count
if __name__ == '__main__':
    s = "0111100010"
    n = len(s)
    m=splitting(s,n)
    print(m)
