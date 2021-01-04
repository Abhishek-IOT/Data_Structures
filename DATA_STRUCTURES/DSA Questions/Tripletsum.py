"""
Triplet sum in Array
Given an array A[] of N numbers and another number x,
determine whether or not there exist three elements in A[] whose sum is exactly x
A = [1, 4, 45, 6, 10, 8]
sum = 22
Ouput-"yes"
Logic first sort the array and then have two pointer accordingly increase and decreace the pointers
until the sum is there
            elif l>k:
                second_pointer=second_pointer-1
            else:
                first_pointer=first_pointer+1

"""


def sort(arr,size):
    for i in range(size):
        for j in range(size):
            if arr[i]<arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print(arr)
def triplet(arr,s,k):
    sort(arr,s)
    l=0
    for i in range(s-2):
        first_pointer=i+1
        second_pointer=s-1
        while(first_pointer<second_pointer):
            l=arr[i]+arr[first_pointer]+arr[second_pointer]
            if l == k:
                return l
            elif l>k:
                second_pointer=second_pointer-1
            else:
                first_pointer=first_pointer+1
    return l





if __name__ == '__main__':
    arr=[1, 4, 45, 6, 10, 8]
    k=22
    # sort(arr,len(arr))
    l=triplet(arr,len(arr),k)
    if l==k:
        print("Yes")
    else:
        print("No")