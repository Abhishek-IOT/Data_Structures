"""
Given an array, cyclically rotate an array by one.
INPUT=1 2 3 4 5
OUPUT=5 1 2 3 4
      OR
OUPUT=2 3 4 5 1
# """
# def rotate(arr):
#     temp=arr[0]
#     for i in range(1,len(arr)):
#         arr[i-1]=arr[i]
#     arr[len(arr)-1]=temp
#     print(arr)
def rotate2(arr):
    temp=arr[0]
    for i in range(len(arr),1):
        arr[i-1]=arr[i]
    print(arr)
def implement(arr):
    arr2=[]
    print(arr[len(arr)-1])
    arr2.append(arr[len(arr)-1])
    for i in range(0,len(arr)-1):
        arr2.append(arr[i])
    print(arr2)
if __name__ == '__main__':
    arr=[1,2,3,4,5]
    # rotate(arr)
    rotate2(arr)
    implement(arr)