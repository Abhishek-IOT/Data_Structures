class Rotation:
    def rotate_left(self,arr,d,n):
        for i in range(d):
            self.rotate(arr,n)
    def rotate(self,arr,n):
        temp=arr[0]
        for i in range(n-1):
            arr[i]=arr[i+1]
        arr[n-1]=temp
    def print_array(self,arr,n):
        for i in range(n):
            print(arr[i])
if __name__ == '__main__':
    rotation=Rotation()
    arr=[1,2,3,4,5,6]
    rotation.rotate_left(arr, 2, len(arr))
    rotation.print_array(arr,len(arr))