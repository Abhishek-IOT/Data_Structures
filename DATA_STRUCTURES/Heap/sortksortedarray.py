from heapq import  heappop,heappush,heapify
def sort_k(arr,k):
    heap=arr[:k+1]
    heapify(heap)
    t=0
    for i in range(k+1,len(arr)):
        arr[t]=heappop(heap)
        heappush(heap,arr[i])
        t=t+1
    while(heap):
        arr[t]=heappop(heap)
        t+=1
if __name__ == '__main__':
    arr=[10,52,0,30,20,12,59,154]
    sort_k(arr,3)
    print(arr)