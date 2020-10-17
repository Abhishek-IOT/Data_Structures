class Min_max:
    def to_findmin(self,arr,size):
        min=arr[0]
        for i in range(1,size):
            if arr[i]<arr[0]:
                min=arr[i]
        return min

    def to_findmax(self, arr, size):
        max = arr[0]
        for i in range(1, size):
            if arr[i] > arr[0]:
                max = arr[i]
        return max
if __name__ == '__main__':
    mode=Min_max()
    arr=[1,5,78,96,86,100]
    max=mode.to_findmax(arr,len(arr))
    min=mode.to_findmin(arr,len(arr))
    print("The maximum element is",max)
    print("the minimum element is",min)
