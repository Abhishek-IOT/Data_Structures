class Selection_sort:
    def sort(self,arr):
        for i in range(len(arr)):
            min_index=i
            for j in range(i+1,len(arr)):
                if arr[min_index]>arr[j]:
                    min_index=j
            temp=arr[i]
            arr[i]=arr[min_index]
            arr[min_index]=temp
        for i in range(len(arr)):
            print(arr[i])
if __name__ == '__main__':
    sorting=Selection_sort()
    arr=[20,4,16,5,9]
    sorting.sort(arr)