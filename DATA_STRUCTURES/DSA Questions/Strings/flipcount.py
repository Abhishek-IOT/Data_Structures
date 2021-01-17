"""
Min Number of Flips
Easy Accuracy: 42.58% Submissions: 7437 Points: 2
Given a binary string, that is it contains only 0s and 1s. We need to make this string a sequence of alternate characters by flipping some of the bits, our goal is to minimize the number of bits to be flipped.
Examples:

Input : str = “001”
Output : 1
Minimum number of flips required = 1
We can flip 1st bit from 0 to 1
Logic=Make a flip function so that we can have the alternate sequence.
getflipcount(s,expect)=We will increment the count if the s[i]!=expect.
Then we will make a function a function which will return the min of flip.
"""
def flip(ch):
    if ch=='0':
        return '1'
    else:
        return '0'
def getflipcount(s,expect):
    flipcount=0
    for i in range(len(s)):
        if s[i]!=expect:
            flipcount+=1
        print(expect,s[i],"i=",i)
        expect=flip(expect)
        print("After",expect,"Filp",flipcount)
    return flipcount
def flipcountforalternate(s):
    return min(getflipcount(s,'0'),getflipcount(s,'1'))
if __name__ == '__main__':
    str = "0001010111"
    print(flipcountforalternate(str))