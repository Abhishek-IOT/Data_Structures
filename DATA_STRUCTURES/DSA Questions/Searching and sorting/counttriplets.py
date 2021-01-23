"""
Count triplets with sum smaller than a given value
Difficulty Level : Medium
 Last Updated : 28 Aug, 2019
Given an array of distinct integers and a sum value. Find count of triplets with sum smaller than given sum value. Expected Time Complexity is O(n2).
Logic=We will use two pointer algorithm for letting the time complexity one ladder down....We will have i fixed and check the next part in i+1 to end subarray.

"""
def counttrip(arr,sum):
    l=len(arr)
    ans=0
    for i in range(l-2):
        j=i+1
        k=l-1
        while(j<k):
            if (arr[i]+arr[j]+arr[k]>=sum):
                k=k-1
            else:
                ans=ans+(k-j)
                j=j+1
    return ans
if __name__ == '__main__':
    arr = [5, 1, 3, 4, 7]
    n = len(arr)
    sum = 10
    print(counttrip(arr, sum))