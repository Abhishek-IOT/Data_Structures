"""
Second most repeated string in a sequence
Easy Accuracy: 34.09% Submissions: 1534 Points: 2
Given a sequence of strings, the task is to find out the second most repeated (or frequent) string in the given sequence.

Note: No two strings are the second most repeated, there will be always a single string.
Logic=Make a Hash map for the string that means make a dictionary with the count of the string then print the 1 character of the
dictionary.
"""

def occuring(s):
    l=len(s)
    data=dict()
    for i in range(l):
        if s[i] in data:
            data[s[i]]+=1
        else:
            data[s[i]]=1
    print(data)
    print(sorted(data))
    name=sorted(data)
    print(name[1])

if __name__ == '__main__':
    s=['aaa', 'bbb', 'ccc', 'bbb', 'aaa', 'aaa']
    occuring(s)