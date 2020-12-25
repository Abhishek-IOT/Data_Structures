"""
Move all negative numbers to beginning and positive to end with constant extra space.
Input=[-1, 2, -3, 4, 5, 6, -7, 8, 9]
Output=[-1, -3, -7, 4, 5, 6, 2, 8, 9]
"""
def move(arr,n):
    j=0
    for i in range(n):
        if (arr[i]<0):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            j=j+1
    print(arr)
if __name__ == '__main__':
    arr=[-1, 2, -3, 4, 5, 6, -7, 8, 9]
    move(arr,len(arr))
