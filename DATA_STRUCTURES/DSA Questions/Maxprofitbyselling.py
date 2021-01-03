"""
In a daily share trading, a buyer buys shares in the morning and sells it on the same day. If the trader is allowed to make at most 2 transactions in a day, whereas the second transaction can only start after the first one is complete (Sell->buy->sell->buy). Given stock prices throughout the day, find out the maximum profit that a share trader could have made.

Examples:

Input:   price[] = {10, 22, 5, 75, 65, 80}
Output:  87
Trader earns 87 as sum of 12 and 75
Buy at price 10, sell at 22, buy at 5 and sell at 80
LOGIC=we have to do arr[i]-arr[i-1] and then just add the value to profit if the value is greater than 0.

"""
def maxpro(arr,size):
    pro=0
    for i in range(1,size):
        sub=arr[i]-arr[i-1]
        if sub>0:
            pro=pro+sub
    return pro
if __name__ == '__main__':
    arr=[100, 30, 15, 10, 8, 25, 80]
    m=maxpro(arr,len(arr))
    print(m)
