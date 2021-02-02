"""
Stickler Thief
Easy Accuracy: 43.3% Submissions: 8860 Points: 2
Stickler the thief wants to loot money from a society having n houses in a single line. He is a weird person and follows a certain rule
when looting the houses. According to the rule, he will never loot two consecutive houses. At the same time, he wants to maximize the amount he loots.
 The thief knows which house has what amount of money but is unable to come up with an optimal looting strategy.
 He asks for your help to find the maximum money he can get if he strictly follows the rule. Each house has a[i] amount of money present in it.
 Logic we will use  dynamic approach and check if the element should be included or not we will do this with dynamic programming.
"""
def maxvalue(arr):
    l=len(arr)
    if l==0:
        return 0
    if l==1:
        return arr[1]
    if l==2:
        return max(arr[0],arr[1])
    dp=[0]*l
    dp[0]=arr[0]
    dp[1]=max(arr[0],arr[1])
    for i in range(2, l):
        dp[i] = max(arr[i] + dp[i - 2], dp[i - 1])

    return dp
if __name__ == '__main__':
    hval = [1,3,4,2,5]

    # number of houses
    n = len(hval)
    print("Maximum loot value : {}".
          format(maxvalue(hval)))
