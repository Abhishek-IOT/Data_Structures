"""
Arithmetic Number
Easy Accuracy: 19.06% Submissions: 4803 Points: 2
Given three integers  'A' denoting the first term of an arithmetic sequence , 'C' denoting the common difference of an arithmetic sequence and an integer 'B'. you need to tell whether 'B' exists in the arithmetic sequence or not.

Example 1:

Input: A = 1, B = 3, C = 2
Output: 1
Explaination: 3 is the second term of the
sequence starting with 1 and having a common
difference 2.
"""
def missing(a,b,c,n):
    for i in range(n+1):
        ap=a+(i-1)*c
        if ap==b:
            return True

if __name__ == '__main__':
    a=1
    b=2
    c=2
    n=2
    yo=missing(a,b,c,n)
    if yo==True:
        print("Yes ")
    else:
        print("No")

