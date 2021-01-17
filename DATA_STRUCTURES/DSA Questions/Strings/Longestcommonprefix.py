"""
14. Longest Common Prefix
Easy

3553

2082

Add to List

Share
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".
Logic=We will make two functions first is commonprefix and other is helper function.Helper function will take
the arguments and check that the prefix are equal or not...if not then it will break...else it will return result.
Then at the last have the largest in length prefix.
"""
def helper(s1,s2):
    l1=len(s1)
    l2=len(s2)
    i=0
    j=0
    result=""
    while i<l1-1 and j<l2-1:
        if s1[i]!=s2[i]:
            break
        result+=s1[i]
        print(result,i)
        i+=1
        j+=1
    return result
def commonprefix(arr,size):
    prefix=arr[0]
    for i in range(size):
        prefix=helper(prefix,arr[i])
        # print(prefix,i)
    return prefix
if __name__ == '__main__':
    arr = ["flower","flow","flight"]
    n = len(arr)

    ans = commonprefix(arr, n)
    if len(ans)>0:
        print("the longest prefix sequence=",ans)
    else:
        print("NO")