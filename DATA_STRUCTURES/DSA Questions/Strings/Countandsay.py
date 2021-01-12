"""
Count and Say
Easy

208

681

Add to List

Share
The count-and-say sequence is a sequence of digit strings defined by the recursive formula:

countAndSay(1) = "1"
countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1), which is then converted into a different digit string.
To determine how you "say" a digit string, split it into the minimal number of groups so that each group is a contiguous section all of the same character.
Then for each group, say the number of characters,
then say the character. To convert the saying into a digit string, replace the counts with a number and concatenate every saying.
Logic make the base case and then iterate from the 3 to len(S) and then add a delimeter and then iterate the string and check if the s[j]!=s[j-1]
append the count and the character and if condition not fullfied increment the counter then.
"""
def countsay(n):
    if n==1:
        return "1"
    if n==2:
        return "11"
    s="11"
    for i in range(3,n+1):
        s=s+"$"
        l=len(s)
        c=1
        temp=""
        for j in range(1,l):
            if(s[j]!=s[j-1]):
                temp+=str(c+0)
                temp=temp+s[j-1]
            else:
                c=c+1
        s=temp
    return s
m=countsay(4)
print(m)
