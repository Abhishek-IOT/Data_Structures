class Bubble_sort:
    def Sort(self,arr):
        length=len(arr)
        for i in  range(length):
            for j in range(length-i-1):
                if arr[j]>arr[j+1]:
                    temp=arr[j]
                    arr[j]=arr[j+1]
                    arr[j+1]=temp
if __name__ == '__main__':
    a=Bubble_sort()
    s=[1,5,4,9,0]
    a.Sort(s)
    print(s)
    for i in range(len(s)):
        print(s[i],end=" ")