"""
Subarray with 0 sum
Given an array of positive and negative numbers.
Find if there is a subarray (of size at-least one) with 0 sum.
Input:
5
4 2 -3 1 6

Output:
Yes

Explanation:
2, -3, 1 is the subarray
with sum 0.
HINT=We will use the data set called set for it
Logic=If the sum is 0 then return 0 else store the sum in set so that if sum is in the set that
means there is an sub array with sum=0
"""
def sum(arr, size):
    s=set()
    sumi = 0
    for i in range(size):
        if arr[i] == 0:
            sumi = 0
            break
        else:
            sumi=sumi+arr[i]
            if sumi==0 or sumi in s:
                return True
            s.add(sumi)
    return False


if __name__ == '__main__':
    arr = [4, 2, -3, 1, 6]
    i = sum(arr, len(arr))
    print(i)
    if i == True:
        print("Yes")
    else:
        print("No")

