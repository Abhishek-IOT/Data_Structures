"""
Minimum characters to be added at front to make string palindrome
Difficulty Level : Hard
 Last Updated : 09 Oct, 2019
Given a string str we need to tell minimum characters to be added at front of string to make string palindrome.

Examples:

Input  : str = "ABC"
Output : 2
We can make above string palindrome as "CBABC"
by adding 'B' and 'C' at front.
Logic=Make a method to check the palindrome.
If the string is not palidrome we will start cutting the last element of the string until the string is palindrome.
and also increase the counter.
We set a flag as 1 when we find the palindrome and then print the count.
"""

def ispalin(s):
    l=len(s)
    i=0
    j=l-1
    while(i<=j):
        if s[i]!=s[j]:
            return False
        i=i+1
        j-=1
    return True
if __name__ == '__main__':
    s = "AACECAAAA"
    count=0
    flag=0
    while(len(s)>0):
        if ispalin(s):
            flag=1
            break
        else:
            count+=1
            s=s[:-1]
    if flag==1:
        print(count)