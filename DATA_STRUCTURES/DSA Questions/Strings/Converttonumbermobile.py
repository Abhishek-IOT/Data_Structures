"""
Convert a sentence into its equivalent mobile numeric keypad sequence
Difficulty Level : Easy
 Last Updated : 06 Nov, 2020
Given a sentence in the form of a string, convert it into its equivalent mobile numeric keypad sequence.
LOgic=Make the dictinory of mobile no and then just check if in dicttionary and print.
"""
def convert(d,s):
    l=len(s)
    for i in range(l):
        if s[i] in d:
            print(d[s[i]],end=" ")
if __name__ == '__main__':
    s='geeksforgeeks'
    d={'a':1,'b':1,'c':1,'d':2,'e':2,'f':2,'g':3,'h':3,'i':3,'j':4,'k':4,'l':4,'m':5,'n':5,'o':5,
       'p':6,'q':6,'r':6,'s':6,'t':7,'u':7,'v':7,'wxyz':9}
    convert(d,s)