"""
 Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
 design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
In this my approach was
1)To Find the first minimum value
2)To find the last maximum value
3)Then substract the maximum and minimum value
4)If the array is sorted in descending order then return 0
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
"""
def getmin(arr,size):
    m = arr[0]
    index = 0
    for i in range(1, size):
        if arr[i] < m:
            m = arr[i]
            index = i
        if index == size - 1:
            # index = 0
            m=0
    return m,index
def getmax(arr,size,intial):
    m=arr[size-1]
    index=1
    i=size-2
    while(i>intial):
        # print(arr[i],m,i)
        if arr[i]>m:
            m=arr[i]
            index=i
        i=i-1
    return m

def maxprofit(arr,size):
    mini=getmin(arr,size)
    print("The minimum value is ",mini[0],"from index",mini[1])
    maxi=getmax(arr,size,mini[1])
    print(maxi,"the maximum value")
    maxpro=maxi-mini[0]
    if mini[1] == size - 1:
        maxpro = 0
    return maxpro
if __name__ == '__main__':
    arr= [1,2,3,4,5]
    m=maxprofit(arr,len(arr))
    print(m)
    # getmax(arr,len(arr),2)
    # print(y)
