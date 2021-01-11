"""
344. Reverse String
Easy

1938

744

Add to List

Share
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
"""
def reverse(arr):
    l=len(arr)
    i=l
    while(i>0):
        print(arr[i-1],end=" ")
        i=i-1
    return arr


if __name__ == '__main__':
    arr=["h","e","l","l","o"]
    r=reverse(arr)
    print(r)
