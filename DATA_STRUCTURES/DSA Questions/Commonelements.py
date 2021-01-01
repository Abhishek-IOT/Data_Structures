"""

Given three arrays sorted in increasing order.
 Find the elements that are common in all three arrays
 Input:
n1 = 6; A = {1, 5, 10, 20, 40, 80}
n2 = 5; B = {6, 7, 20, 80, 100}
n3 = 8; C = {3, 4, 15, 20, 30, 70, 80, 120}
Output: 20 80
Explanation: 20 and 80 are the only
common elements in A, B and C.
If x, y and z are same, we can simply print any of them as common element and move ahead in all three arrays.
Else If x < y, we can move ahead in ar1[] as x cannot be a common element.
Else If x > z and y > z), we can simply move ahead in ar3[] as z cannot be a common element.
"""


def common(a1,a2,a3,n1,n2,n3):
    i,j,k=0,0,0
    while(i<n1 and j<n2 and k<n3):
        print(ar1[i],i,"Value of i")
        print(ar2[j],j,"Value of j")
        print(ar3[k],k,"Value of k")
        if a1[i]==a2[j] and a2[j]==a3[k]:
            print(a1[i])
            i=i+1
            j=j+1
            k=k+1
        elif a1[i]<a2[j]:
            i=i+1
        elif a2[j]<a3[k]:
            j=j+1
        else:
            k=k+1
    # print(i,j,k)
if __name__ == '__main__':
    ar1 = [1, 5, 10, 20, 40, 80]
    ar2 = [6, 7, 20, 80, 100]
    ar3 = [3, 4, 15, 20, 30, 70, 80, 120]
    n1 = len(ar1)
    n2 = len(ar2)
    n3 = len(ar3)
    print("Common elements are")
    common(ar1, ar2, ar3, n1, n2, n3)
