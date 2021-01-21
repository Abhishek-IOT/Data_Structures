"""
Find Pair Given Difference
Easy Accuracy: 47.62% Submissions: 16791 Points: 2
Given an unsorted array Arr[] and a number N. You need to write a program to
 find if there exists a pair of elements in the array whose difference is N.
Logic=Have two counter and check that the difference is equal or not ,if not then check if greater then
increase j counter else increase i counter.

"""
def pair(arr,size,n):
    i,j=0,1
    while i<size and j<size:
        if i!=j and arr[j]-arr[i]==n:
            print("The pair found",arr[i],arr[j])
            return True
        elif arr[j]-arr[i]<n:
            j=j+1
        else:
            i=i+1
    return False
if __name__ == '__main__':
    arr=[1, 8, 30, 40, 100]
    n=60
    m=pair(arr,len(arr),n)
    if m==True:
        print("Yes")
    else:
        print("no")