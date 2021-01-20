"""
Print all subsequences of a string in Python
Last Updated : 20 Aug, 2020
Given a string, we have to find out all subsequences of it. A String is a subsequence of a given String, that
is generated by deleting some character of a given string without changing its order.
Logic=First check start==size if yes then print string else first use temp without a and second time with a
"""

def printall(temp,start,size,s):
    if start==size:
        print(temp)
    else:
        printall(temp,start+1,size,s)
        temp=temp+s[start]
        printall(temp,start+1,size,s)
if __name__ == '__main__':
    s="abc"
    printall("",0,len(s),s)
    # print(len(s))



