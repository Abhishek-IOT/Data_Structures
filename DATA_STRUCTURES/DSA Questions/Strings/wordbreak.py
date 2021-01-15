"""
Word Break Problem | DP-32
Difficulty Level : Hard
 Last Updated : 02 Sep, 2019
Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. See following examples for more details.
This is a famous Google interview question, also being asked by many other companies now a days.

Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice,
  cream, icecream, man, go, mango}

Input:  ilike
Output: Yes
The string can be segmented as "i like".
Logic=
"""
def wordbreak(d,s,out="1"):
    if not s:
        print(out)
    for i in range(1,len(s)+1):
        prefix=s[:i]
        print("Orefix=",prefix)
        if prefix in d:
            wordbreak(d,s[i:],out+" "+prefix)
if __name__ == '__main__':
    dict = ['i', 'like', 'sam', 'sung', 'samsung']
    str = "ilike"
    wordbreak(dict,str)
