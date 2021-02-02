# def count(i,j,s):
#
#     if i>j:
#         return 0
#     if i==j:
#         return 1
#     if dp[i][j]!=-1:
#         return dp[i][j]
#     if s[i]==s[j]:
#         dp[i][j]=count(i+1,j,s)+count(i,j-1,s)+1
#         return dp
#     else:
#         dp[i][j]=count(i+1,j,s)+count(i,j-1,s)-count(i+1,j-1,s)
#         return dp
#
#
# if __name__ == '__main__':
#     s="abcd"
#     dp=[[-1 for i in range(len(s)) ]for j in range(len(s))]
#     print(dp)
#     count(0,len(s)-1,s)
