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
if __name__ == '__main__':
    arr=[1,2,3,4,5]
    rotate(arr)
    rotate2(arr)