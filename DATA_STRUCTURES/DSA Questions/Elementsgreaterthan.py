"""
Given an array of size n and a number k, find all elements that appear more than n/k times
Given an array of size n, find all elements in array that appear more than n/k times.
 For example, if the input arrays is {3, 1, 2, 2, 1, 2, 3, 3} and k is 4, then the output should be [2, 3]. Note that size of array is 8 (or n = 8),
 so we need to find all elements that appear more than 2 (or 8/4) times. There are two elements that appear more than two times, 2 and 3.
LOGIC=To find the count of each element and then check that it is more than n//k if so then print it.
"""

def elements(arr,n,k):
    d=n//k
    freq={}
    for i in range(n):
        if arr[i] in freq:
            freq[arr[i]]=freq[arr[i]]+1
        else:
            freq[arr[i]]=1
    for i in freq:
        if freq[i]>d:
            print(i)
    print(freq)
if __name__ == '__main__':
    arr = [1, 1, 2, 2, 3, 5, 4, 2, 2, 3, 1, 1, 1]
    k=4
    elements(arr,len(arr),k)