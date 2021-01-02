"""
Factorials of large numbers
Given an integer, the task is to find factorial of the number.

Input:
The first line of input contains an integer T denoting the number of test cases.
The first line of each test case is N,the number whose factorial is to be found

Output:
Print the factorial of the number in separate line
"""

def factorial(inp):
    if inp==1:
        return 1
    else:
        return inp*factorial(inp-1)
if __name__ == '__main__':
    test=int(input())
    f=[]
    for i in range(test):
        inp=int(input())
        fact=factorial(inp)
        f.append(fact)
    for i in range(len(f)):
        print(f[i])